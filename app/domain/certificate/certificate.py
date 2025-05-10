# app/domain/certificate.py
from pydantic import BaseModel

class Certificate(BaseModel):
    participant_name: str
    exam_code: str
    score: float
    date: str
