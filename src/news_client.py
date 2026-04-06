"""
news_client.py

Fetches recent entries from RSS feeds focused on AI-assisted mathematical
research and saves keyword-filtered results to data/latest_news.json.
"""

import calendar
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

import feedparser
import requests

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"
OUTPUT_PATH = DATA_DIR / "latest_news.json"

# ---------------------------------------------------------------------------
# Feed sources
# Focused on AI + formal mathematics, theorem proving, and ML for math.
# ---------------------------------------------------------------------------
FEEDS = [
    # Formal theorem proving & Lean ecosystem
    {
        "url": "https://leanprover-community.github.io/blog/rss.xml",
        "name": "Lean Community Blog",
    },
    {
        "url": "https://xenaproject.wordpress.com/feed/",
        "name": "Xena Project (Kevin Buzzard)",
    },
    {
        "url": "https://math.andrej.com/feed.xml",
        "name": "Mathematics and Computation (Andrej Bauer)",
    },
    # AI labs doing math research
    {
        "url": "https://deepmind.google/blog/rss.xml",
        "name": "Google DeepMind Blog",
    },
    {
        "url": "https://blog.research.google/feeds/posts/default",
        "name": "Google Research Blog",
    },
    {
        "url": "https://bair.berkeley.edu/blog/feed.xml",
        "name": "BAIR Blog",
    },
    # Notable math researchers blogging on AI
    {
        "url": "https://terrytao.wordpress.com/feed/",
        "name": "Terence Tao — What's New",
    },
    # AI4Math community
    {
        "url": "https://frenzymath.com/rss.xml",
        "name": "FrenzyMath (AI4M Team, BICMR@PKU)",
    },
    # Computational mathematics
    {
        "url": "https://blog.wolfram.com/feed/",
        "name": "Wolfram Blog",
    },
    # AI labs with active math/reasoning research
    {
        "url": "https://openai.com/blog/rss.xml",
        "name": "OpenAI Blog",
    },
    {
        "url": "https://huggingface.co/blog/feed.xml",
        "name": "Hugging Face Blog",
    },
    {
        "url": "https://www.microsoft.com/en-us/research/feed/",
        "name": "Microsoft Research Blog",
    },
]

CUTOFF_DAYS = 14

# ---------------------------------------------------------------------------
# Keyword filter — two tiers:
#   TITLE_KEYWORDS: broader terms matched only against the title (low noise).
#   KEYWORDS: specific phrases matched against title + summary.
# An item is kept if it matches either list.
# ---------------------------------------------------------------------------

# Broad terms — safe to match in titles only
TITLE_KEYWORDS = [
    "math", "maths", "mathematics", "mathematical",
    "geometry", "geometric", "topology", "topological",
    "algebra", "algebraic",
    "theorem", "proof", "conjecture",
    "physics", "quantum",
    "reasoning", "reasoning model",
]

KEYWORDS = [
    # Formal proof / theorem proving
    "lean 4", "lean4", "mathlib", "coq", "isabelle", "agda",
    "formal proof", "formal verification", "theorem proving", "proof assistant",
    "automated theorem", "interactive theorem",
    "formalization", "certified proof", "proof search", "proof generation",
    "proof synthesis",
    # AI + math intersection
    "ai for math", "ai in math", "machine learning for math",
    "neural theorem", "alphaproof", "alphageometry", "minerva",
    "llm math", "language model math",
    "mathematical reasoning", "math reasoning",
    "ai reasoning", "chain of thought",
    "mathematical discovery", "scientific discovery",
    "math olympiad", "imo problem",
    "math benchmark", "gsm8k", "amc ", "aime ",
    "deep think",
    # AI models known for math — specific phrases to avoid product noise
    "gemini deep think", "gemini for math", "gemini math",
    "o3 math", "o4 math",
    "openai o3", "openai o4", "openai o1",
    # Relevant math CS topics
    "sat solver", "smt solver", "type theory", "homotopy type",
    "constructive math", "computability",
    # Physics / math AI crossover
    "symbolic computation", "computer algebra", "automated mathematics",
    # General AI + science
    "ai-assisted", "ai assisted", "accelerating math", "accelerating science",
]


# ---------------------------------------------------------------------------
# Date parsing
# ---------------------------------------------------------------------------
def parse_entry_date(entry) -> datetime | None:
    """Try to extract a timezone-aware datetime from a feedparser entry."""
    struct = getattr(entry, "published_parsed", None) or getattr(
        entry, "updated_parsed", None
    )
    if struct:
        try:
            ts = calendar.timegm(struct)
            return datetime.fromtimestamp(ts, tz=timezone.utc)
        except Exception:
            pass

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
    """Return a clean, single-line summary."""
    raw = (
        getattr(entry, "summary", None)
        or getattr(entry, "description", None)
        or ""
    )
    return " ".join(raw.split())


# ---------------------------------------------------------------------------
# Keyword filter
# ---------------------------------------------------------------------------
def matches_keywords(title: str, summary: str) -> list[str]:
    """Return the list of matched keywords (empty = no match).

    TITLE_KEYWORDS are checked against the title only (broader terms).
    KEYWORDS are checked against title + summary (specific phrases).
    """
    title_lower = title.lower()
    full_text = (title + " " + summary).lower()
    matched = [kw for kw in TITLE_KEYWORDS if kw in title_lower]
    matched += [kw for kw in KEYWORDS if kw in full_text and kw not in matched]
    return matched


# ---------------------------------------------------------------------------
# Per-feed fetch
# ---------------------------------------------------------------------------
def fetch_feed(feed_cfg: dict, cutoff: datetime) -> list[dict]:
    url = feed_cfg["url"]
    name = feed_cfg["name"]
    print(f"  [{name}] {url}")

    # Use requests for fetching so that certifi handles SSL correctly on all
    # platforms, then pass the raw content to feedparser for parsing.
    try:
        resp = requests.get(url, timeout=20, headers={"User-Agent": "research-sentinel/1.0"})
        resp.raise_for_status()
        feed = feedparser.parse(resp.content)
    except requests.exceptions.RequestException as e:
        print(f"    [warning] Could not fetch feed: {e}")
        return []

    if feed.bozo and not feed.entries:
        print(f"    [warning] Parse issue: {feed.bozo_exception}")

    recent = 0
    kept = []

    for entry in feed.entries:
        pub_date = parse_entry_date(entry)

        if pub_date is None:
            date_str = "unknown"
        else:
            if pub_date < cutoff:
                continue
            date_str = pub_date.strftime("%Y-%m-%d")

        recent += 1
        title = entry.get("title", "").strip()
        summary = extract_summary(entry)
        matched = matches_keywords(title, summary)

        if not matched:
            continue

        kept.append({
            "title": title,
            "link": entry.get("link", "").strip(),
            "published_date": date_str,
            "summary": summary,
            "source_name": name,
            "source_feed": url,
            "matched_keywords": matched,
        })
        print(f"    + Kept: {title[:80]!r}  (matched: {matched[:3]})")

    print(f"    -> {recent} recent, {len(kept)} kept after keyword filter.")
    return kept


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    cutoff = datetime.now(tz=timezone.utc) - timedelta(days=CUTOFF_DAYS)
    print(f"Fetching {len(FEEDS)} feeds — entries since {cutoff.date()}.\n")

    all_items: list[dict] = []

    for feed_cfg in FEEDS:
        try:
            items = fetch_feed(feed_cfg, cutoff)
            all_items.extend(items)
        except Exception as exc:
            print(f"    [error] Failed: {feed_cfg['url']!r}: {exc}")

    print(f"\nTotal items after keyword filter: {len(all_items)}")

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(all_items, f, indent=2, ensure_ascii=False)

    print(f"Saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
