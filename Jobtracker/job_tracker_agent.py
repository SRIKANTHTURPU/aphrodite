"""
Hyderabad QA/SDET Job Tracker Agent
------------------------------------
Fetches live job postings from the Adzuna API (India), filters for roles
matching your stack (Playwright, Cypress, Selenium, Appium, TypeScript, SDET),
de-duplicates against jobs already seen in previous runs, and appends only
NEW postings into your existing GCC_Job_Application_Tracker.xlsx file.

Why this avoids "false alerts":
- Adzuna's API returns live, structured listings with real apply links
  (not scraped/stale copies).
- This script keeps its own local memory (seen_jobs.json) of every job ID
  it has already shown you, so you only ever see genuinely NEW postings,
  not the same job re-surfacing on every run.
- You control the keyword/location filtering yourself, instead of trusting
  a third-party alert engine's matching logic.

SETUP (one-time):
1. Go to https://developer.adzuna.com/ and sign up for a free account.
   You'll instantly get an App ID and App Key -- no credit card needed.
2. Set them as environment variables before running:
     export ADZUNA_APP_ID="your_app_id_here"
     export ADZUNA_APP_KEY="your_app_key_here"
   (On Windows: set ADZUNA_APP_ID=your_app_id_here / set ADZUNA_APP_KEY=...)
3. Install dependencies:
     pip install requests openpyxl --break-system-packages
4. Run it:
     python3 job_tracker_agent.py

RUNNING IT REGULARLY:
- Linux/Mac: add a cron job, e.g. run daily at 9am:
    0 9 * * * cd /path/to/script && python3 job_tracker_agent.py
- Windows: use Task Scheduler to run it daily.
- Each run only reports/appends jobs it hasn't seen before.

FILES THIS SCRIPT CREATES/USES (in the same folder):
- seen_jobs.json          -> memory of job IDs already reported (do not delete
                             unless you want to re-see everything as "new")
- new_jobs_found.csv      -> running log of every new job ever found, with date
- GCC_Job_Application_Tracker.xlsx -> your existing tracker; new rows get
                             appended to the "Application Tracker" sheet
                             (place a copy of your tracker in this same folder,
                             or edit TRACKER_PATH below to point to it)
"""

import os
import json
import csv
import sys
from datetime import datetime

import requests

# ---------------------------------------------------------------------------
# CONFIG -- edit these if needed
# ---------------------------------------------------------------------------

APP_ID = os.environ.get("ADZUNA_APP_ID", "")
APP_KEY = os.environ.get("ADZUNA_APP_KEY", "")

COUNTRY = "in"                # India
LOCATION = "Hyderabad"
RESULTS_PER_PAGE = 50
MAX_PAGES = 3                 # up to 150 results per keyword per run

# Search terms -- each is run as a separate Adzuna query for better recall
SEARCH_TERMS = [
    "SDET",
    "QA Automation Engineer",
    "Test Automation Engineer",
    "Quality Engineer Playwright",
    "Automation Engineer Cypress",
]

# A posting must contain at least one of these (case-insensitive) in its
# title or description to be considered relevant to your actual stack.
# This is the filter that keeps out generic/irrelevant "QA" noise.
RELEVANCE_KEYWORDS = [
    "playwright", "cypress", "selenium", "appium", "robot framework",
    "typescript", "sdet", "test automation", "qa automation",
]

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SEEN_JOBS_PATH = os.path.join(SCRIPT_DIR, "seen_jobs.json")
NEW_JOBS_LOG_PATH = os.path.join(SCRIPT_DIR, "new_jobs_found.csv")
TRACKER_PATH = os.path.join(SCRIPT_DIR, "GCC_Job_Application_Tracker.xlsx")

ADZUNA_BASE_URL = "https://api.adzuna.com/v1/api/jobs/{country}/search/{page}"


# ---------------------------------------------------------------------------
# CORE LOGIC
# ---------------------------------------------------------------------------

def load_seen_jobs():
    if os.path.exists(SEEN_JOBS_PATH):
        with open(SEEN_JOBS_PATH, "r", encoding="utf-8") as f:
            return set(json.load(f))
    return set()


def save_seen_jobs(seen_ids):
    with open(SEEN_JOBS_PATH, "w", encoding="utf-8") as f:
        json.dump(sorted(seen_ids), f, indent=2)


def fetch_jobs_for_term(term):
    """Fetch all pages of results for one search term from Adzuna."""
    all_results = []
    for page in range(1, MAX_PAGES + 1):
        url = ADZUNA_BASE_URL.format(country=COUNTRY, page=page)
        params = {
            "app_id": APP_ID,
            "app_key": APP_KEY,
            "what": term,
            "where": LOCATION,
            "results_per_page": RESULTS_PER_PAGE,
            "content-type": "application/json",
        }
        try:
            resp = requests.get(url, params=params, timeout=20)
            resp.raise_for_status()
        except requests.RequestException as e:
            print(f"  [warn] request failed for '{term}' page {page}: {e}")
            break

        data = resp.json()
        results = data.get("results", [])
        if not results:
            break
        all_results.extend(results)

        # Stop paging early if we've already fetched everything available
        if len(results) < RESULTS_PER_PAGE:
            break

    return all_results


def is_relevant(job):
    text = f"{job.get('title', '')} {job.get('description', '')}".lower()
    return any(kw in text for kw in RELEVANCE_KEYWORDS)


def dedupe_and_filter(raw_jobs, seen_ids):
    """Return only new, relevant jobs; also returns their ids to mark as seen."""
    new_jobs = []
    new_ids = set()
    for job in raw_jobs:
        job_id = str(job.get("id"))
        if not job_id or job_id in seen_ids or job_id in new_ids:
            continue
        if not is_relevant(job):
            continue
        new_jobs.append(job)
        new_ids.add(job_id)
    return new_jobs, new_ids


def append_to_csv_log(new_jobs):
    file_exists = os.path.exists(NEW_JOBS_LOG_PATH)
    with open(NEW_JOBS_LOG_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(
                ["Date Found", "Company", "Title", "Location", "Salary", "Apply URL"]
            )
        for job in new_jobs:
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M"),
                job.get("company", {}).get("display_name", ""),
                job.get("title", ""),
                job.get("location", {}).get("display_name", ""),
                job.get("salary_min", "") or "",
                job.get("redirect_url", ""),
            ])


def append_to_excel_tracker(new_jobs):
    """Append new jobs as rows in the existing Excel tracker, if present."""
    if not os.path.exists(TRACKER_PATH):
        print(f"  [info] No tracker found at {TRACKER_PATH} -- skipping Excel update.")
        print("         (Place a copy of GCC_Job_Application_Tracker.xlsx in this folder to enable this.)")
        return

    try:
        import openpyxl
        from openpyxl.styles import Font, PatternFill, Border, Side
    except ImportError:
        print("  [warn] openpyxl not installed -- skipping Excel update. "
              "Run: pip install openpyxl --break-system-packages")
        return

    wb = openpyxl.load_workbook(TRACKER_PATH)
    ws = wb["Application Tracker"]

    # find first fully empty row (column A blank) to start appending
    r = 5
    while ws.cell(row=r, column=1).value:
        r += 1

    FONT = "Arial"
    normal_font = Font(name=FONT, size=10)
    new_font = Font(name=FONT, size=10, bold=True, color="1F4E78")
    fill = PatternFill(start_color="DDEBF7", end_color="DDEBF7", fill_type="solid")
    thin = Side(style="thin", color="D9D9D9")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)

    for job in new_jobs:
        company = job.get("company", {}).get("display_name", "Unknown")
        title = job.get("title", "")
        url = job.get("redirect_url", "")

        ws.cell(row=r, column=1, value=company).font = new_font
        ws.cell(row=r, column=5, value="Adzuna API").font = normal_font
        ws.cell(row=r, column=8, value="Not Applied").font = normal_font
        ws.cell(row=r, column=13, value=f"Auto-found: {title} | {url}").font = normal_font
        for col in range(1, 14):
            ws.cell(row=r, column=col).border = border
            if col == 1:
                ws.cell(row=r, column=col).fill = fill
        r += 1

    wb.save(TRACKER_PATH)
    print(f"  [ok] Appended {len(new_jobs)} new job(s) to {TRACKER_PATH}")


def main():
    if not APP_ID or not APP_KEY:
        print("ERROR: ADZUNA_APP_ID and ADZUNA_APP_KEY environment variables are not set.")
        print("Get a free key at https://developer.adzuna.com/ and set them before running.")
        sys.exit(1)

    seen_ids = load_seen_jobs()
    print(f"Loaded {len(seen_ids)} previously-seen job IDs.")

    all_raw_jobs = []
    for term in SEARCH_TERMS:
        print(f"Searching Adzuna for: '{term}' in {LOCATION}...")
        results = fetch_jobs_for_term(term)
        print(f"  -> {len(results)} raw results")
        all_raw_jobs.extend(results)

    new_jobs, new_ids = dedupe_and_filter(all_raw_jobs, seen_ids)

    print(f"\n{len(new_jobs)} NEW relevant job(s) found this run.\n")

    for job in new_jobs:
        company = job.get("company", {}).get("display_name", "Unknown")
        title = job.get("title", "")
        url = job.get("redirect_url", "")
        print(f"- [{company}] {title}\n    {url}")

    if new_jobs:
        append_to_csv_log(new_jobs)
        append_to_excel_tracker(new_jobs)

    seen_ids.update(new_ids)
    save_seen_jobs(seen_ids)
    print(f"\nDone. Total jobs now remembered: {len(seen_ids)}")


if __name__ == "__main__":
    main()
