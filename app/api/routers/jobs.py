from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app.schemas import JobCreate, JobResponse
from app.services import job_service

router = APIRouter(prefix="/jobs", tags=["Jobs"])


@router.post("/", response_model=JobResponse)
async def create_new_job(
    job: JobCreate, user_id: int, db: AsyncSession = Depends(get_db)
):
    return await job_service.create_job(db, job, user_id)


@router.get("/", response_model=list[JobResponse])
async def get_jobs_list(db: AsyncSession = Depends(get_db)):
    return await job_service.get_all_jobs(db)
