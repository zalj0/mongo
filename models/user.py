from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    device_id: str
    name: str
    type: str
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    serial_number: Optional[str] = None
    installed_at: Optional[str] = None