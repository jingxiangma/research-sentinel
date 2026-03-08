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
        papers_prompt = f"""You are an expert mathematician in algebraic geometry and theoretical physics.

Below is a JSON list of recent ArXiv papers:

{json.dumps(papers, indent=2)}

Task: Write a short Markdown paragraph (3-6 sentences, no heading) summarising which of these papers \
are most relevant to Hodge atoms, K-equivalence, derived categories, or quantum D-modules. \
For each relevant paper mention its title, authors, and ArXiv URL as a Markdown link. \
If none are directly relevant, write one sentence saying so. \
Output only the raw Markdown paragraph — no preamble, no headings."""

        print("Generating ArXiv highlights...")
        highlights = ollama_chat(papers_prompt)
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
