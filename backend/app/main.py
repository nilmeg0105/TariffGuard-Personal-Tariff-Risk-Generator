from fastapi import Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Job
from typing import Optional


app = FastAPI(title="ScrapeX Job Market API")


@app.get("/jobs")
def get_jobs(
    search: Optional[str] = Query(None),
    location: Optional[str] = Query(None),
    company: Optional[str] = Query(None),
    page: int = 1,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    query = db.query(Job)

    if search:
        query = query.filter(Job.job_title.ilike(f"%{search}%"))

    if location:
        query = query.filter(Job.location.ilike(f"%{location}%"))

    if company:
        query = query.filter(Job.company.ilike(f"%{company}%"))

    total = query.count()

    jobs = (
        query
        .offset((page - 1) * limit)
        .limit(limit)
        .all()
    )

    return {
        "total": total,
        "page": page,
        "limit": limit,
        "jobs": jobs
    }

