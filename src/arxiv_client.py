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
def _run_search(
    client: arxiv.Client,
    query: str,
    sort_by: arxiv.SortCriterion,
    cutoff: datetime,
    keywords: list[str],
    title_only_keywords: list[str],
    date_field: str,
    seen_urls: set[str],
    label: str,
    max_results: int = 500,
) -> list[dict]:
    """Run a single ArXiv search and return matched papers not already in seen_urls."""
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=sort_by,
        sort_order=arxiv.SortOrder.Descending,
    )

    results = []
    total_fetched = 0

    for paper in client.results(search):
        published = paper.published
        if published.tzinfo is None:
            published = published.replace(tzinfo=timezone.utc)

        updated = paper.updated
        if updated.tzinfo is None:
            updated = updated.replace(tzinfo=timezone.utc)

        ref_date = updated if date_field == "updated" else published
        if ref_date < cutoff:
            if date_field == "submitted":
                # Results are sorted by submission date; safe to stop early.
                log.info(
                    f"[{label}] Reached papers older than cutoff "
                    f"({cutoff.date()}) after {total_fetched} scanned. Stopping."
                )
                break
            total_fetched += 1
            continue

        total_fetched += 1

        if paper.entry_id in seen_urls:
            continue

        combined_text = f"{paper.title} {paper.summary}"
        matched = find_matched_keywords(combined_text, keywords)
        matched += find_matched_keywords(paper.title, title_only_keywords)

        if not matched:
            continue

        seen_urls.add(paper.entry_id)
        results.append(
            {
                "title": paper.title,
                "authors": [a.name for a in paper.authors],
                "published_date": published.strftime("%Y-%m-%d"),
                "updated_date": updated.strftime("%Y-%m-%d"),
                "summary": paper.summary.replace("\n", " ").strip(),
                "arxiv_url": paper.entry_id,
                "matched_keywords": matched,
            }
        )
        log.info(f"  + Kept: {paper.title[:80]!r} (matched: {matched})")

    log.info(
        f"[{label}] {total_fetched} papers scanned, {len(results)} kept."
    )
    return results


def fetch_papers(topic: dict, cutoff: datetime) -> list[dict]:
    """
    Fetch papers for a single topic config block and return filtered results.
    Runs two searches per topic: one sorted by submission date (new papers)
    and one sorted by last-updated date (recently revised papers).

    Args:
        topic:  One entry from config['topics'], with 'name', 'categories',
                and 'keywords' keys.
        cutoff: Only keep papers submitted or revised on or after this datetime.
    """
    name = topic["name"]
    categories = topic["categories"]
    keywords = topic.get("keywords", [])
    title_only_keywords = topic.get("title_only_keywords", [])

    query = build_category_query(categories)

    client = arxiv.Client(
        page_size=200,
        delay_seconds=3,
        num_retries=3,
    )

    seen_urls: set[str] = set()

    log.info(f"[{name}] Search 1/2 — new papers (sorted by submission date)")
    results = _run_search(
        client, query, arxiv.SortCriterion.SubmittedDate,
        cutoff, keywords, title_only_keywords, "submitted", seen_urls, name,
    )

    log.info(f"[{name}] Search 2/2 — revised papers (sorted by last-updated date)")
    results += _run_search(
        client, query, arxiv.SortCriterion.LastUpdatedDate,
        cutoff, keywords, title_only_keywords, "updated", seen_urls, name,
        max_results=2000,
    )

    log.info(
        f"[{name}] Done — {len(results)} total papers kept after both searches."
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
