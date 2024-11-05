from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/health", tags=["헬스체크"])


class OkResponse(BaseModel):
    """
    dto : data transger object
    데이터"만" 담고 있는 객체이다.(데이터를 변형도 한다면 dto가 아님)
    (parsing까지는 봐주는 경우가 있긴 함... e.g.) "i: -> i)
    """

    ok: bool
    extra_msg: str | None = None


@router.post("", response_model=OkResponse)
async def health() -> OkResponse:  # path operation function
    return OkResponse(ok=True)
