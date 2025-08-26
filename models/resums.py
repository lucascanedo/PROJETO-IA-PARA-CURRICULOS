from pydantic import BaseModel

class Resums(BaseModel):
    id: str
    job_id: str
    content: str
    opnion: str
    file: str