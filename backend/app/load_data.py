import pandas as pd
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from .database import SessionLocal
from .models import Job

CSV_PATH = "../data/cleaned_jobs.csv"


def safe(val):
    """Convert NaN / NaT to None"""
    if pd.isna(val):
        return None
    return val


def load_csv_to_db():
    db: Session = SessionLocal()
    df = pd.read_csv(CSV_PATH)

    inserted = 0

    for _, row in df.iterrows():
        job = Job(
            job_title=safe(row.get("job_title")),
            company=safe(row.get("company")),
            location=safe(row.get("location")),
            employment_type=safe(row.get("type")),
            source=safe(row.get("source")),
            min_salary=parse_salary_min(row.get("salary")),
            max_salary=parse_salary_max(row.get("salary")),
            currency=parse_currency(row.get("salary")),
            posted_date=parse_date(row.get("posted")),
            job_url=safe(row.get("job_url")),
            description=safe(row.get("description_preview")),
            scraped_at=datetime.now(timezone.utc)
        )

        db.add(job)
        inserted += 1

    db.commit()
    db.close()

    print(f"Inserted {inserted} jobs into database.")


def parse_salary_min(s):
    if pd.isna(s):
        return None
    nums = [int(x) for x in str(s).split() if x.isdigit()]
    return nums[0] if nums else None


def parse_salary_max(s):
    if pd.isna(s):
        return None
    nums = [int(x) for x in str(s).split() if x.isdigit()]
    return nums[-1] if len(nums) > 1 else None


def parse_currency(s):
    if pd.isna(s):
        return None
    for cur in ["USD", "INR", "EUR"]:
        if cur in str(s):
            return cur
    return None


def parse_date(d):
    try:
        if pd.isna(d):
            return None
        return pd.to_datetime(d).date()
    except:
        return None


if __name__ == "__main__":
    load_csv_to_db()
