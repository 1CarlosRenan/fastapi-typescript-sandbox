from fastapi import APIRouter
from ..models.views.user import UserOut

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[UserOut])
async def get_users():
    return []
