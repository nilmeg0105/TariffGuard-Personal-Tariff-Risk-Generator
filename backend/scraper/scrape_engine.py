import pandas as pd
from backend.scraper.scrape_router import detect_source_type
from backend.scraper.bs4_job_scraper import scrape_static_jobs
import requests

def scrape_api(url):
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    jobs = data.get("jobs", [])

    processed = []
    for job in jobs:
        processed.append({
            "Job Title": job.get("title", "N/A"),
            "Company": job.get("companyName", "N/A"),
            "Location": "Remote",
            "Type": job.get("employmentType", "N/A"),
            "Salary": job.get("minSalary", "N/A"),
            "Job URL": job.get("applicationLink", "N/A")
        })

    return pd.DataFrame(processed)

def scrape(url):
    source_type = detect_source_type(url)
    print(f"[ScrapeX] Detected source type: {source_type}")

    if source_type == "static":
        return scrape_static_jobs(url)

    elif source_type == "api":
        return scrape_api(url)

    else:
        raise NotImplementedError("Dynamic scraping currently disabled due to anti-bot")

if __name__ == "__main__":
    test_urls = [
        "https://realpython.github.io/fake-jobs/",
        "https://himalayas.app/jobs/api?category=software-engineering"
    ]

    for url in test_urls:
        df = scrape(url)
        print(df.head())
