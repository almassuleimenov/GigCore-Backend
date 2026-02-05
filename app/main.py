import uvicorn
from fastapi import FastAPI
from app.api import user_router, job_router

app = FastAPI(
    title="FreelanceHunter",
    description="Platform for hiring professionals",
    version="1.0.0",
)

app.include_router(user_router)
app.include_router(job_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
