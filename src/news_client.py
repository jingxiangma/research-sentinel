"""
news_client.py

Fetches recent entries from hardcoded RSS feeds and saves results to
data/latest_news.json.
"""

import json
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import feedparser

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"
OUTPUT_PATH = DATA_DIR / "latest_news.json"

# ---------------------------------------------------------------------------
# Feed sources
# ---------------------------------------------------------------------------
FEED_URLS = [
    "https://openai.com/blog/rss.xml",
    "https://leanprover-community.github.io/blog/index.xml",
    "https://bair.berkeley.edu/blog/feed.xml",
]

CUTOFF_DAYS = 7


# ---------------------------------------------------------------------------
# Date parsing
# ---------------------------------------------------------------------------
def parse_entry_date(entry) -> datetime | None:
    """
    Try to extract a timezone-aware datetime from a feedparser entry.

    feedparser normalises dates into a 9-tuple (published_parsed or
    updated_parsed) using time.struct_time.  Falls back to the raw string
    if the parsed field is absent.
    """
    struct = getattr(entry, "published_parsed", None) or getattr(
        entry, "updated_parsed", None
    )
    if struct:
        try:
            # time.mktime() assumes local time; use calendar.timegm for UTC
            import calendar
            ts = calendar.timegm(struct)
            return datetime.fromtimestamp(ts, tz=timezone.utc)
        except Exception:
            pass

    # Fallback: try parsing the raw string
    for attr in ("published", "updated"):
        raw = getattr(entry, attr, None)
        if raw:
            for fmt in (
                "%a, %d %b %Y %H:%M:%S %z",
                "%a, %d %b %Y %H:%M:%S GMT",
                "%Y-%m-%dT%H:%M:%S%z",
                "%Y-%m-%dT%H:%M:%SZ",
            ):
                try:
                    dt = datetime.strptime(raw.strip(), fmt)
                    if dt.tzinfo is None:
                        dt = dt.replace(tzinfo=timezone.utc)
                    return dt
                except ValueError:
                    continue

    return None


# ---------------------------------------------------------------------------
# Summary extraction
# ---------------------------------------------------------------------------
def extract_summary(entry) -> str:
    """Return a clean, single-line summary from whichever field is available."""
    raw = (
        getattr(entry, "summary", None)
        or getattr(entry, "description", None)
        or ""
    )
    return " ".join(raw.split())  # collapse whitespace / newlines


# ---------------------------------------------------------------------------
# Per-feed fetch
# ---------------------------------------------------------------------------
def fetch_feed(url: str, cutoff: datetime) -> list[dict]:
    print(f"  Fetching: {url}")
    feed = feedparser.parse(url)

    if feed.bozo:
        # bozo=True means feedparser hit a parse error; surface it but continue
        print(f"    [warning] Feed parse issue: {feed.bozo_exception}")

    entries_found = 0
    kept = []

    for entry in feed.entries:
        pub_date = parse_entry_date(entry)

        if pub_date is None:
            # Can't determine age — include conservatively
            print(f"    [warning] Could not parse date for entry: {entry.get('title', '?')!r}")
            date_str = "unknown"
        else:
            if pub_date < cutoff:
                continue
            date_str = pub_date.strftime("%Y-%m-%d")

        entries_found += 1
        kept.append(
            {
                "title": entry.get("title", "").strip(),
                "link": entry.get("link", "").strip(),
                "published_date": date_str,
                "summary": extract_summary(entry),
                "source_feed": url,
            }
        )

    print(f"    -> {entries_found} recent article(s) found.")
    return kept


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    cutoff = datetime.now(tz=timezone.utc) - timedelta(days=CUTOFF_DAYS)
    print(f"Fetching RSS feeds — keeping entries from the last {CUTOFF_DAYS} days (since {cutoff.date()}).\n")

    all_items: list[dict] = []

    for url in FEED_URLS:
        try:
            items = fetch_feed(url, cutoff)
            all_items.extend(items)
        except Exception as exc:
            print(f"    [error] Failed to process feed {url!r}: {exc}")

    print(f"\nTotal articles collected: {len(all_items)}")

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(all_items, f, indent=2, ensure_ascii=False)

    print(f"Saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
