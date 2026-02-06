from app.api.routers.users import router as user_router
from app.api.routers.jobs import router as job_router
from app.api.routers.auth import router as auth_router

__all__ = [
    "user_router",
    "job_router",
    "auth_router",
]
