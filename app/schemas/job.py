from pydantic import BaseModel, ConfigDict, Field
from app.models import JobStatus
from typing import Annotated


class JobBase(BaseModel):
    title: Annotated[str, Field(title="Title about job/task")]
    description: Annotated[str, Field(title="Description about job/task")]
    budget: Annotated[int, Field(title="Budget for solve task/job")]


class JobCreate(JobBase):
    pass


class JobResponse(JobBase):
    id: Annotated[int, Field(title="JOB number")]
    status: Annotated[JobStatus, Field(title="Status about task")]
    author_id: Annotated[int, Field(title="Author ID")]

    model_config = ConfigDict(from_attributes=True)
