from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Job, JobStatus
from app.schemas import JobCreate


async def create_job(session: AsyncSession, job_in: JobCreate, author_id: int):

    new_job = Job(
        **job_in.model_dump(),
        author_id=author_id,
        status=JobStatus.OPEN,
    )

    session.add(new_job)
    await session.commit()
    await session.refresh(new_job)
    return new_job


async def get_all_jobs(session: AsyncSession) -> list[Job]:
    query = select(Job)
    result = await session.execute(query)
    return result.scalars().all()
