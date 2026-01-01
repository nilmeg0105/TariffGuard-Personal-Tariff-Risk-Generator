from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium_stealth
import pandas as pd
import time

# Main remote jobs page - apply filters manually or via code if needed
URL = "https://himalayas.app/jobs/remote"

def scrape_himalayas_jobs(url):
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    # Comment out for visible browser/debugging
    # options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)

    selenium_stealth.stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    try:
        driver.get(url)
        time.sleep(10)  # Initial load

        # Optional: Scroll to load more jobs (infinite scroll common)
        print("Scrolling to load more jobs...")
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            time.sleep(4)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # Job cards: typically <article> or <div> with role="article" or class containing "job"
        job_cards = driver.find_elements(By.CSS_SELECTOR, "article, div[class*='job'], a[href*='/jobs/']")

        print(f"Found {len(job_cards)} potential job elements.")

        jobs = []
        for card in job_cards:
            try:
                # Title + URL
                title_elem = card.find_element(By.CSS_SELECTOR, "h3, h2, a strong, [class*='title']")
                title = title_elem.text.strip()
                job_url = card.find_element(By.TAG_NAME, "a").get_attribute("href")

                # Company
                company = "N/A"
                try:
                    company = card.find_element(By.CSS_SELECTOR, "[class*='company'], p strong").text.strip()
                except:
                    pass

                # Location/Tags/Salary
                tags = "Remote"
                try:
                    tag_elems = card.find_elements(By.CSS_SELECTOR, "span.badge, small, [class*='tag'], [class*='salary']")
                    tags += " | " + " | ".join([t.text.strip() for t in tag_elems if t.text.strip()])
                except:
                    pass

                jobs.append({
                    "Job Title": title,
                    "Company": company,
                    "Tags/Location/Salary": tags,
                    "Job URL": job_url
                })

            except Exception as e:
                continue  # Skip malformed cards

        df = pd.DataFrame(jobs)
        return df

    finally:
        driver.quit()

if __name__ == "__main__":
    df = scrape_himalayas_jobs(URL)

    if not df.empty:
        print(f"Scraped {len(df)} remote jobs from Himalayas!")
        print(df.head(10))

        csv_path = r"C:\Users\mega6\OneDrive\Desktop\Scrape\data\himalayas_jobs_selenium.csv"
        df.to_csv(csv_path, index=False)
        print(f"Saved to {csv_path}")
    else:
        print("No jobs found. Try running without headless, apply filters manually (e.g., search 'software engineer' or 'internship'), or increase scroll loops.")
        print("Tip: Sign up for free on the site in the browser for more personalized/full listings.")