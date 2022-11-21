from fastapi import APIRouter
from ..models.groups import Group

router = APIRouter(prefix="/groups", tags=["Groups"])


@router.get("/", response_model=list[Group])
async def get_groups():
    return []
