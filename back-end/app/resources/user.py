from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    email: str
    created_ts: datetime
    updated_ts: Optional[datetime]



