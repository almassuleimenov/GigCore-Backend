import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import user_router, job_router, auth_router

app = FastAPI(
    title="FreelanceHunter",
    description="Platform for hiring professionals",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],      
    allow_headers=["*"],      
)

app.include_router(user_router)
app.include_router(job_router)
app.include_router(auth_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)