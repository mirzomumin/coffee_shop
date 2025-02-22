from fastapi import APIRouter
from src.api.v1.routers.users import router as router_user


router = APIRouter(prefix="/v1")

router.include_router(router_user, tags=["users"])
