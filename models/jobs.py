from pydantic import BaseModel

class Job(BaseModel):
    id: str
    name: str
    main_activities: str
    prerequisities: str
    differentials: str