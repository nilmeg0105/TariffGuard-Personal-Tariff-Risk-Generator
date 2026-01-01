from scraper.scrape_router import detect_source_type

urls = [
    "https://realpython.github.io/fake-jobs/",
    "https://himalayas.app/jobs/api",
    "https://example.com"
]

for url in urls:
    print(url, "→", detect_source_type(url))
