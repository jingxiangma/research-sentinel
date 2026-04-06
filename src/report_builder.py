"""
report_builder.py

Reads data/latest_papers.json and data/latest_news.json and writes
human-readable Markdown reports to docs/latest_papers.md and docs/latest_news.md.
"""

import json
import os
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"

PAPERS_JSON = DATA_DIR / "latest_papers.json"
NEWS_JSON = DATA_DIR / "latest_news.json"
PAPERS_MD = DOCS_DIR / "latest_papers.md"
NEWS_MD = DOCS_DIR / "latest_news.md"


def load_json(path: Path) -> list:
    if not path.exists():
        print(f"Warning: {path} not found — skipping.")
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_papers_md(papers: list, generated_date: str) -> str:
    lines = [
        "# Latest ArXiv Papers",
        "",
        f"_Generated on {generated_date} — {len(papers)} paper(s) matched._",
        "",
        "---",
        "",
    ]

    if not papers:
        lines.append("_No papers found for this period._")
        return "\n".join(lines)

    for i, p in enumerate(papers, 1):
        authors = ", ".join(p.get("authors", []))
        title = p.get("title", "Untitled")
        url = p.get("arxiv_url", "")
        pub_date = p.get("published_date", "unknown date")
        summary = p.get("summary", "")
        keywords = p.get("matched_keywords", [])

        lines.append(f"## {i}. [{title}]({url})")
        lines.append("")
        lines.append(f"**Authors:** {authors}  ")
        lines.append(f"**Published:** {pub_date}  ")
        if keywords:
            lines.append(f"**Matched keywords:** {', '.join(f'`{k}`' for k in keywords)}")
        lines.append("")
        lines.append("> " + summary.replace("\n", " "))
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def build_news_md(news: list, generated_date: str) -> str:
    lines = [
        "# Latest Research News",
        "",
        f"_Generated on {generated_date} — {len(news)} item(s) collected._",
        "",
        "---",
        "",
    ]

    if not news:
        lines.append("_No news items found for this period._")
        return "\n".join(lines)

    # Group by source feed for readability
    by_source: dict[str, list] = {}
    for item in news:
        source = item.get("source_feed", "Unknown")
        by_source.setdefault(source, []).append(item)

    for source, items in by_source.items():
        # Extract a short display name from the feed URL
        source_name = source.split("/")[2] if "/" in source else source
        site_url = f"https://{source_name}" if source_name != source else source
        lines.append(f"## [{source_name}]({site_url})")
        lines.append("")

        for item in items:
            title = item.get("title", "Untitled")
            link = item.get("link", "")
            pub_date = item.get("published_date", "unknown date")
            summary = item.get("summary", "")

            if link:
                lines.append(f"### [{title}]({link})")
            else:
                lines.append(f"### {title}")
            lines.append("")
            lines.append(f"**Date:** {pub_date}")
            lines.append("")
            # Trim very long summaries to first 400 characters
            display_summary = summary[:400] + ("…" if len(summary) > 400 else "")
            lines.append(display_summary)
            lines.append("")

        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def main():
    today = date.today().isoformat()
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    papers = load_json(PAPERS_JSON)
    news = load_json(NEWS_JSON)

    papers_md = build_papers_md(papers, today)
    with open(PAPERS_MD, "w", encoding="utf-8") as f:
        f.write(papers_md)
    print(f"Written: {PAPERS_MD}  ({len(papers)} papers)")

    news_md = build_news_md(news, today)
    with open(NEWS_MD, "w", encoding="utf-8") as f:
        f.write(news_md)
    print(f"Written: {NEWS_MD}  ({len(news)} news items)")


if __name__ == "__main__":
    main()
