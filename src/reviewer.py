import json
import os
import re
import requests
from datetime import date

LIT_REVIEW_PATH = "docs/lit_review.md"
PAPERS_PATH = "data/latest_papers.json"
NEWS_PATH = "data/latest_news.json"
CHANGELOG_PATH = "docs/changelog.md"
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2"

HIGHLIGHTS_TAG = "<!-- BEGIN:ARXIV_HIGHLIGHTS -->"
HIGHLIGHTS_END_TAG = "<!-- END:ARXIV_HIGHLIGHTS -->"
AI_SECTION_HEADER = "## 5. AI and Formal Methods in Mathematics"

# Papers matching ANY of these keywords are always surfaced in the highlights
# block verbatim, regardless of what the LLM selects. Guards against the LLM
# missing core lit-review topics (the Verra-fourfold / Hodge-atom paper of
# Apr 2026 was missed this way).
PRIORITY_KEYWORDS = [
    "Hodge atoms",
    "noncommutative minimal model program",
    "homological minimal model program",
    "birational invariant",
    "perverse schober",
    "spherical functor",
    "semiorthogonal decomposition",
    "semi-orthogonal decomposition",
    "quantum D-module",
    "Chen-Ruan cohomology",
    "GKZ system",
    "rationality problem",
    "modular symbols",
]


def load_file(path):
    if not os.path.exists(path):
        print(f"Error: file not found: {path}")
        return None
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def ollama_chat(prompt):
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=300)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        print(f"Error: could not connect to Ollama at {OLLAMA_URL}. Is it running?")
        exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Error: Ollama request failed: {e}")
        exit(1)
    return response.json()["message"]["content"].strip()


def find_priority_papers(papers: list) -> list:
    """Return papers whose matched_keywords intersect PRIORITY_KEYWORDS."""
    priority_set = {kw.lower() for kw in PRIORITY_KEYWORDS}
    result = []
    for p in papers:
        matched = [kw.lower() for kw in p.get("matched_keywords", [])]
        if any(kw in priority_set for kw in matched):
            result.append(p)
    return result


def build_priority_block(papers: list) -> str:
    """Render a deterministic bullet list of priority papers for the highlights block."""
    if not papers:
        return ""
    lines = ["**Auto-flagged high-priority matches (keyword-pinned):**", ""]
    for p in papers:
        title = p.get("title", "Untitled").replace("\n", " ").strip()
        url = p.get("arxiv_url", "")
        authors = ", ".join(p.get("authors", []))
        matched = p.get("matched_keywords", [])
        kw_str = ", ".join(f"`{k}`" for k in matched)
        lines.append(f"- [{title}]({url}) — {authors}. Matched: {kw_str}.")
    lines.append("")
    return "\n".join(lines)


def merge_highlights(review: str, highlights: str) -> str:
    """Replace the tagged highlights block if present, otherwise append it to Section 4."""
    block = f"{HIGHLIGHTS_TAG}\n{highlights}\n{HIGHLIGHTS_END_TAG}"
    if HIGHLIGHTS_TAG in review:
        return re.sub(
            re.escape(HIGHLIGHTS_TAG) + r".*?" + re.escape(HIGHLIGHTS_END_TAG),
            block,
            review,
            flags=re.DOTALL,
        )
    # Append before Section 5 if it exists, otherwise at end of Section 4 area
    if AI_SECTION_HEADER in review:
        return review.replace(AI_SECTION_HEADER, block + "\n\n" + AI_SECTION_HEADER)
    return review.rstrip() + "\n\n" + block + "\n"


def merge_ai_section(review: str, ai_section: str) -> str:
    """Replace existing Section 5 or append it at the end."""
    if AI_SECTION_HEADER in review:
        # Remove everything from Section 5 header to end, then re-append
        idx = review.index(AI_SECTION_HEADER)
        return review[:idx].rstrip() + "\n\n" + ai_section + "\n"
    return review.rstrip() + "\n\n" + ai_section + "\n"


def main():
    lit_review = load_file(LIT_REVIEW_PATH)
    if lit_review is None:
        exit(1)

    papers_raw = load_file(PAPERS_PATH)
    if papers_raw is None:
        exit(1)

    try:
        papers = json.loads(papers_raw)
    except json.JSONDecodeError as e:
        print(f"Error: could not parse {PAPERS_PATH}: {e}")
        exit(1)

    # Load news — missing file is non-fatal
    news = []
    if os.path.exists(NEWS_PATH):
        try:
            with open(NEWS_PATH, "r", encoding="utf-8") as f:
                news = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            print(f"Warning: could not load {NEWS_PATH}: {e}. Continuing without news.")

    if not papers and not news:
        print("No new papers or news to review.")
        exit(0)

    updated_review = lit_review

    # --- Pass 1: ArXiv highlights ---
    if papers:
        priority_papers = find_priority_papers(papers)
        priority_urls = {p.get("arxiv_url") for p in priority_papers}
        other_papers = [p for p in papers if p.get("arxiv_url") not in priority_urls]
        priority_block = build_priority_block(priority_papers)
        print(f"Priority papers auto-flagged: {len(priority_papers)}")

        papers_prompt = f"""You are an expert mathematician in algebraic geometry and theoretical physics.

Below is a JSON list of recent ArXiv papers (papers already flagged as
high-priority by keyword match have been excluded from this list):

{json.dumps(other_papers, indent=2)}

Task: Write a short Markdown paragraph (3-6 sentences, no heading) summarising which of these papers \
are most relevant to Hodge atoms, K-equivalence, derived categories, quantum D-modules, perverse \
schobers, the noncommutative minimal model program, or rationality problems. \
For each relevant paper mention its title, authors, and ArXiv URL as a Markdown link. \
If none are directly relevant, write one sentence saying so. \
Output only the raw Markdown paragraph — no preamble, no headings."""

        print("Generating ArXiv highlights narrative...")
        narrative = ollama_chat(papers_prompt) if other_papers else ""
        highlights = (priority_block + "\n" + narrative).strip() if priority_block else narrative
        updated_review = merge_highlights(updated_review, highlights)
        print("  Done.")

    # --- Pass 2: AI & Formal Methods section ---
    if news:
        news_prompt = f"""You are a mathematician tracking AI tools applied to mathematics.

Below is a JSON list of recent news items from AI research blogs:

{json.dumps(news, indent=2)}

Task: Write a Markdown section for a literature review. \
The section must start with the exact heading: {AI_SECTION_HEADER!r}. \
Include only items relevant to: AI reasoning, formal theorem proving (e.g. Lean 4), \
or machine learning applied to mathematics. \
For each relevant item include: a brief description and a Markdown link to the original URL. \
If nothing is relevant, write a single sentence under the heading saying so. \
Output only the raw Markdown — no preamble, no extra commentary."""

        print("Generating AI & Formal Methods section...")
        ai_section = ollama_chat(news_prompt)
        # Ensure the heading is present even if the model dropped it
        if AI_SECTION_HEADER not in ai_section:
            ai_section = AI_SECTION_HEADER + "\n\n" + ai_section
        updated_review = merge_ai_section(updated_review, ai_section)
        print("  Done.")

    with open(LIT_REVIEW_PATH, "w", encoding="utf-8") as f:
        f.write(updated_review)

    today = date.today().isoformat()
    changelog_entry = (
        f"\n## {today}\n\n"
        f"Literature review updated with {len(papers)} new paper(s) and "
        f"{len(news)} news item(s) via Ollama ({MODEL}).\n"
    )
    with open(CHANGELOG_PATH, "a", encoding="utf-8") as f:
        f.write(changelog_entry)

    print(f"Review updated and saved to {LIT_REVIEW_PATH}.")
    print(f"Changelog entry appended to {CHANGELOG_PATH}.")


if __name__ == "__main__":
    main()
