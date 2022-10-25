from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    id: Optional[int] = None
    created_date: Optional[datetime] = datetime.now()

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'created_date': str(self.created_date)
        }

