import json
import os
import requests
from datetime import date

LIT_REVIEW_PATH = "docs/lit_review.md"
PAPERS_PATH = "data/latest_papers.json"
NEWS_PATH = "data/latest_news.json"
CHANGELOG_PATH = "docs/changelog.md"
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2"


def load_file(path):
    if not os.path.exists(path):
        print(f"Error: file not found: {path}")
        return None
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


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

    prompt = f"""You are an expert mathematician specializing in algebraic geometry and theoretical physics, \
with deep knowledge of Hodge theory, K-equivalence, derived categories, and quantum D-modules.

Below is the current literature review in Markdown format:

<current_review>
{lit_review}
</current_review>

Below is a JSON list of new ArXiv papers to evaluate:

<new_papers>
{json.dumps(papers, indent=2)}
</new_papers>

Below is a JSON list of recent news items to evaluate:

<news_items>
{json.dumps(news, indent=2)}
</news_items>

Instructions:
1. Determine whether any of the new papers address the "Current Open Problems" section or advance \
the "State of the Art" with respect to Hodge atoms, K-equivalence, derived categories, or quantum D-modules.
2. If relevant papers are found, rewrite the necessary sections of the literature review to integrate \
the new findings accurately and concisely.
3. In addition to updating the math sections based on the ArXiv papers, check the provided "News Items". \
If there are relevant updates regarding AI reasoning, formal theorem proving (like Lean 4), or machine \
learning applied to math, create or update a section titled \
"## 5. AI and Formal Methods in Mathematics" at the bottom of the review.
4. Return ONLY the raw Markdown text of the complete updated literature review. \
Do not include any introductory text, explanations, or conversational remarks — just the Markdown."""

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

    data = response.json()
    updated_review = data["message"]["content"]

    with open(LIT_REVIEW_PATH, "w", encoding="utf-8") as f:
        f.write(updated_review)

    today = date.today().isoformat()
    changelog_entry = f"\n## {today}\n\nLiterature review updated with {len(papers)} new paper(s) and {len(news)} news item(s) via Ollama ({MODEL}).\n"
    with open(CHANGELOG_PATH, "a", encoding="utf-8") as f:
        f.write(changelog_entry)

    print(f"Review updated and saved to {LIT_REVIEW_PATH}.")
    print(f"Changelog entry appended to {CHANGELOG_PATH}.")


if __name__ == "__main__":
    main()
