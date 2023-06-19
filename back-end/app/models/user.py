from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import uuid



@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    public_id: str = None
    id: Optional[int] = None
    created_date: Optional[datetime] = datetime.now()

    def __post_init__(self):
        if not self.public_id:
            self.public_id = User._generate_unique_id()

    @staticmethod
    def _generate_unique_id():
        return str(uuid.uuid4())

