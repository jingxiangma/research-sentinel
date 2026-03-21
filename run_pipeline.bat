@echo off
cd /d "C:\Users\jingx\Documents\claude_projects\research-sentinel"

echo [%date% %time%] Starting Research Sentinel pipeline... >> logs\pipeline.log

C:\Python314\python.exe src/arxiv_client.py >> logs\pipeline.log 2>&1
C:\Python314\python.exe src/news_client.py >> logs\pipeline.log 2>&1
C:\Python314\python.exe src/report_builder.py >> logs\pipeline.log 2>&1

git add docs/latest_papers.md docs/latest_news.md docs/changelog.md data/latest_papers.json data/latest_news.json
git diff --cached --quiet || git commit -m "chore: weekly literature review update [skip ci]"
git push >> logs\pipeline.log 2>&1

echo [%date% %time%] Pipeline complete. >> logs\pipeline.log
