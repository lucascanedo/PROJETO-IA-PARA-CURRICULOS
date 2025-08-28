from pydantic import BaseModel

class Resums(BaseModel):
    resum_id: str
    job_id: str
    content: str
    opnion: str
    file: str