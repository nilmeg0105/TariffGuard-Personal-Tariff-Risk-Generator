from typing import Optional
from pydantic import BaseModel

class JobQuery(BaseModel):
    search: Optional[str] = None
    location: Optional[str] = None
    company: Optional[str] = None
    page: int = 1
    limit: int = 20
