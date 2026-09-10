# Hyderabad QA/SDET Job Tracker Agent

A small script that checks for **genuinely new** QA/SDET/Automation job postings
in Hyderabad, using the free Adzuna API — and only shows you jobs you haven't
already seen, so there's no repeat noise or false alerts.

## Why this instead of Naukri/LinkedIn email alerts?

- Adzuna's API returns **live, structured data** with real apply links — not
  scraped or stale copies.
- The script remembers every job ID it has already shown you (in `seen_jobs.json`),
  so re-running it never re-reports the same posting.
- You control the keyword filter yourself (Playwright, Cypress, Selenium, Appium,
  TypeScript, SDET) — no black-box matching algorithm deciding what counts as
  "relevant" for you.

## One-time setup

1. **Get a free Adzuna API key** (instant, no card needed):
   Go to https://developer.adzuna.com/ → sign up → copy your **App ID** and **App Key**.

2. **Set them as environment variables:**

   On Mac/Linux:
   ```bash
   export ADZUNA_APP_ID="your_app_id_here"
   export ADZUNA_APP_KEY="your_app_key_here"
   ```

   On Windows (Command Prompt):
   ```cmd
   set ADZUNA_APP_ID=your_app_id_here
   set ADZUNA_APP_KEY=your_app_key_here
   ```

   (To make these permanent, add the `export` lines to your `~/.bashrc` or
   `~/.zshrc`, or set them as Windows System Environment Variables.)

3. **Install the two required Python packages:**
   ```bash
   pip install requests openpyxl --break-system-packages
   ```

4. **Put a copy of your `GCC_Job_Application_Tracker.xlsx`** in the same folder
   as `job_tracker_agent.py`. If it's there, new jobs get automatically appended
   as new rows in the "Application Tracker" sheet, tagged with "Adzuna API" as
   the source. If it's not there, the script still works — it'll just skip the
   Excel step and rely on the CSV log instead.

## Running it

```bash
python3 job_tracker_agent.py
```

Each run will:
1. Search Adzuna for SDET / QA Automation / Test Automation roles in Hyderabad.
2. Filter out anything that doesn't mention Playwright, Cypress, Selenium,
   Appium, Robot Framework, TypeScript, or SDET/test automation explicitly.
3. Compare against everything it has shown you before.
4. Print only the NEW matches to your terminal.
5. Log them to `new_jobs_found.csv` (a permanent running history).
6. Append them as new rows in your Excel tracker, if present.

## Running it automatically (recommended)

**Mac/Linux — cron job, runs daily at 9 AM:**
```bash
crontab -e
```
Add this line (edit the path to wherever you saved the script):
```
0 9 * * * cd /path/to/script/folder && /usr/bin/python3 job_tracker_agent.py >> job_tracker.log 2>&1
```

**Windows — Task Scheduler:**
1. Open Task Scheduler → Create Basic Task
2. Trigger: Daily, at your preferred time
3. Action: Start a program → `python.exe` with argument `job_tracker_agent.py`
   and "Start in" set to the script's folder

## Files this creates

| File | Purpose |
|---|---|
| `seen_jobs.json` | Memory of job IDs already reported — don't delete unless you want a fresh start |
| `new_jobs_found.csv` | Permanent log of every new job ever found, with the date it was first seen |
| `GCC_Job_Application_Tracker.xlsx` | Your existing tracker — gets new rows appended automatically |

## Adjusting the search

Open `job_tracker_agent.py` and edit near the top:
- `SEARCH_TERMS` — the job titles/phrases searched for
- `RELEVANCE_KEYWORDS` — the skills that must appear for a job to count as relevant
- `LOCATION` — currently "Hyderabad"; change if you want to widen the search
- `MAX_PAGES` — how many pages of results to pull per search term (50 jobs/page)

## Free tier limits

Adzuna's free tier allows 1,000 API calls per month. This script uses roughly
`5 search terms × up to 3 pages = 15 calls per run`. Running it once daily uses
about 450 calls/month — comfortably within the free tier.
