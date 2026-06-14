@echo off
setlocal

cd /d "%~dp0"
if not exist logs mkdir logs

set "LOG=logs\pipeline.log"
set "PYTHONUTF8=1"
echo [%date% %time%] Starting Research Sentinel pipeline... >> "%LOG%"

set "PYTHON=%LocalAppData%\Programs\Python\Python313\python.exe"
if not exist "%PYTHON%" set "PYTHON=python.exe"
"%PYTHON%" --version >nul 2>&1
if errorlevel 1 (
    echo [%date% %time%] ERROR: A usable Python interpreter was not found. >> "%LOG%"
    exit /b 1
)

where git.exe >nul 2>&1
if errorlevel 1 (
    echo [%date% %time%] ERROR: git.exe was not found on PATH. >> "%LOG%"
    exit /b 1
)

"%PYTHON%" src/arxiv_client.py >> "%LOG%" 2>&1 || goto :failed
"%PYTHON%" src/news_client.py >> "%LOG%" 2>&1 || goto :failed
"%PYTHON%" src/reviewer.py >> "%LOG%" 2>&1 || goto :failed
"%PYTHON%" src/report_builder.py >> "%LOG%" 2>&1 || goto :failed

git add docs/lit_review.md docs/latest_papers.md docs/latest_news.md docs/changelog.md data/latest_papers.json data/latest_news.json
git diff --cached --quiet || git commit -m "chore: weekly literature review update [skip ci]" >> "%LOG%" 2>&1
git push >> "%LOG%" 2>&1 || goto :failed

echo [%date% %time%] Pipeline complete. >> "%LOG%"
exit /b 0

:failed
echo [%date% %time%] ERROR: Pipeline failed with exit code %errorlevel%. >> "%LOG%"
exit /b 1
