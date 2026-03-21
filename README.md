# Research Sentinel

A self-updating literature review tool for **Geometry, Mathematical Physics, and AI**.

Every week, it fetches recent papers from ArXiv and posts from research blogs, then uses a local LLM (via [Ollama](https://ollama.com)) to synthesize the findings into a living Markdown document — automatically kept up to date in this repository.

---

## How It Works

```
config.yaml
    │
    ▼
arxiv_client.py  ──────────────────────► data/latest_papers.json ──┐
                                                                     ├──► reviewer.py ──► docs/lit_review.md
news_client.py   ──────────────────────► data/latest_news.json  ──┘              └──► docs/changelog.md
```

| Script | What it does |
|---|---|
| `src/arxiv_client.py` | Queries ArXiv for papers matching your keywords, saves results to `data/latest_papers.json` |
| `src/news_client.py` | Fetches posts from research RSS feeds (OpenAI, Lean Prover, BAIR), saves to `data/latest_news.json` |
| `src/reviewer.py` | Sends both files to a local Ollama model, which rewrites `docs/lit_review.md` to integrate new findings |

The review itself lives in [`docs/lit_review.md`](docs/lit_review.md) and every update is logged in [`docs/changelog.md`](docs/changelog.md).

---

## Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com) running locally with the `llama3.2` model pulled:
  ```bash
  ollama pull llama3.2
  ```

---

## Installation

```bash
git clone https://github.com/jingxiangma/research-sentinel.git
cd research-sentinel
pip install -r requirements.txt
```

---

## Usage

Run the three scripts in order:

```bash
# 1. Fetch recent ArXiv papers
python src/arxiv_client.py

# 2. Fetch recent news from RSS feeds
python src/news_client.py

# 3. Update the literature review with the local LLM
python src/reviewer.py
```

The updated review will be written to `docs/lit_review.md`.

---

## Configuration

Edit `config.yaml` to control which ArXiv categories and keywords are tracked:

```yaml
topics:
  - name: "Geometry and Physics"
    categories: ["math.AG", "math.SG", "math-ph", "hep-th"]
    keywords:
      - "Homological Mirror Symmetry (HMS)"
      - "Calabi-Yau threefolds"
      - "Stability Condition"
      # add or remove keywords freely
```

- **`categories`** — ArXiv category codes to search within
- **`keywords`** — case-insensitive filters applied to each paper's title and abstract; only papers matching at least one keyword are kept

To change the look-back window (default: 7 days), edit the `timedelta` in `src/arxiv_client.py` and `CUTOFF_DAYS` in `src/news_client.py`.

To switch the LLM model, change `MODEL` at the top of `src/reviewer.py`.

---

## Outputs

| File | Description |
|---|---|
| `docs/lit_review.md` | The living literature review, rewritten each run |
| `docs/changelog.md` | Append-only log of every update with date and paper/news counts |
| `data/latest_papers.json` | Raw ArXiv results from the most recent fetch |
| `data/latest_news.json` | Raw news items from the most recent RSS fetch |

---

## Automated Weekly Runs

The pipeline runs automatically every Monday at 9:00am via **Windows Task Scheduler** (task name: `ResearchSentinel_WeeklyUpdate`). If the computer is off at that time, the task runs on next boot.

The task executes `run_pipeline.bat`, which:
1. Runs the three pipeline scripts in order
2. Commits and pushes all updated files to GitHub

Logs are written to `logs/pipeline.log`.

**Manage the task:**
```powershell
# Run immediately
Start-ScheduledTask -TaskName "ResearchSentinel_WeeklyUpdate"

# Disable
Disable-ScheduledTask -TaskName "ResearchSentinel_WeeklyUpdate"

# Re-enable
Enable-ScheduledTask -TaskName "ResearchSentinel_WeeklyUpdate"
```

The GitHub Actions workflow (`.github/workflows/weekly_update.yml`) is not in use — the pipeline runs fully locally. It is kept as a reference for future migration to a cloud setup.

---

## License

MIT — see [LICENSE](LICENSE).
