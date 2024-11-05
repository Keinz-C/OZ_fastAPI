from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/like", tags=["좋아요"])


class LikeRequest(BaseModel):
    id: int
    article_id: int


class LikeResponse(BaseModel):
    id: int
    article_id: int


@router.post("", response_model=LikeResponse)
async def do_like(like_request: LikeRequest) -> LikeResponse:  # path operation function
    return LikeResponse(id=1, article_id=like_request.article_id)
