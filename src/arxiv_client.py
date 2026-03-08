"""
arxiv_client.py

Fetches recent ArXiv papers matching configured topics/keywords and saves
results to data/latest_papers.json.
"""

import json
import logging
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

import arxiv
import yaml

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).parent.parent
CONFIG_PATH = ROOT / "config.yaml"
DATA_DIR = ROOT / "data"
OUTPUT_PATH = DATA_DIR / "latest_papers.json"

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
def load_config(path: Path) -> dict:
    log.info(f"Loading config from {path}")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


# ---------------------------------------------------------------------------
# Query building
# ---------------------------------------------------------------------------
def build_category_query(categories: list[str]) -> str:
    """Return an ArXiv query string that ORs together the given categories."""
    parts = [f"cat:{cat}" for cat in categories]
    return " OR ".join(parts)


# ---------------------------------------------------------------------------
# Keyword filtering
# ---------------------------------------------------------------------------
def find_matched_keywords(text: str, keywords: list[str]) -> list[str]:
    """Return all keywords (case-insensitive) that appear in text."""
    lowered = text.lower()
    return [kw for kw in keywords if kw.lower() in lowered]


# ---------------------------------------------------------------------------
# Core fetch + filter logic
# ---------------------------------------------------------------------------
def fetch_papers(topic: dict, cutoff: datetime) -> list[dict]:
    """
    Fetch papers for a single topic config block and return filtered results.

    Args:
        topic:  One entry from config['topics'], with 'name', 'categories',
                and 'keywords' keys.
        cutoff: Only keep papers published on or after this datetime.
    """
    name = topic["name"]
    categories = topic["categories"]
    keywords = topic["keywords"]

    query = build_category_query(categories)
    log.info(f"[{name}] Querying ArXiv: {query!r}")

    client = arxiv.Client(
        page_size=200,
        delay_seconds=3,
        num_retries=3,
    )

    search = arxiv.Search(
        query=query,
        max_results=500,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )

    results = []
    total_fetched = 0

    for paper in client.results(search):
        # ArXiv returns results in descending date order; stop once we go past
        # the cutoff window to avoid scanning the entire archive.
        published = paper.published
        if published.tzinfo is None:
            published = published.replace(tzinfo=timezone.utc)

        if published < cutoff:
            log.info(
                f"[{name}] Reached papers older than cutoff "
                f"({cutoff.date()}) after {total_fetched} fetched. Stopping."
            )
            break

        total_fetched += 1
        combined_text = f"{paper.title} {paper.summary}"
        matched = find_matched_keywords(combined_text, keywords)

        if not matched:
            continue

        results.append(
            {
                "title": paper.title,
                "authors": [a.name for a in paper.authors],
                "published_date": published.strftime("%Y-%m-%d"),
                "summary": paper.summary.replace("\n", " ").strip(),
                "arxiv_url": paper.entry_id,
                "matched_keywords": matched,
            }
        )
        log.info(f"  + Kept: {paper.title[:80]!r} (matched: {matched})")

    log.info(
        f"[{name}] Done — {total_fetched} papers fetched, "
        f"{len(results)} kept after keyword filter."
    )
    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    config = load_config(CONFIG_PATH)
    topics = config.get("topics", [])

    cutoff = datetime.now(tz=timezone.utc) - timedelta(days=7)
    log.info(f"Cutoff date: {cutoff.date()} (last 7 days)")

    all_papers: list[dict] = []

    for topic in topics:
        try:
            papers = fetch_papers(topic, cutoff)
            all_papers.extend(papers)
        except Exception as exc:
            log.error(f"Failed to fetch topic {topic.get('name', '?')!r}: {exc}")

    # Deduplicate by arxiv URL in case topics overlap
    seen: set[str] = set()
    unique_papers: list[dict] = []
    for paper in all_papers:
        url = paper["arxiv_url"]
        if url not in seen:
            seen.add(url)
            unique_papers.append(paper)

    log.info(
        f"Total unique papers after deduplication: {len(unique_papers)} "
        f"(from {len(all_papers)} total)"
    )

    # Save output
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(unique_papers, f, indent=2, ensure_ascii=False)

    log.info(f"Saved {len(unique_papers)} papers to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
