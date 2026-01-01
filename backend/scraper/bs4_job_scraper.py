import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://realpython.github.io/fake-jobs/"

def scrape_static_jobs(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    job_cards = soup.find_all("div", class_="card-content")

    jobs = []

    for job in job_cards:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()

        jobs.append({
            "Job Title": title,
            "Company": company,
            "Location": location
        })

    return pd.DataFrame(jobs)

if __name__ == "__main__":
    df = scrape_static_jobs(URL)
    print(df.head())
    df.to_csv("C:\\Users\\mega6\\OneDrive\\Desktop\\Scrape\\data\\static_jobs.csv", index=False)
