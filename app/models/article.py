from __future__ import annotations

from tortoise import Model, fields

from app.models.base_model import BaseModel


class Article(
    BaseModel, Model
):  # 다중 상속, Model로 부터 3개 컬럼을 상속, 나머지는 BaseModel로 부터

    # mysql에서는 varchar타입으로 생성됨.
    # length 255로 하는 이유 -> 255 미만의 varchar는 어차피 길이 255로 생성되서(mysql의 특징)
    # 더 줄여봤자 성능상의 이점이 없기 때문에 할당
    author = fields.CharField(max_length=255)
    title = fields.CharField(max_length=255)

    # 게시글의 본문 생성
    body = fields.TextField()
    # 텍스트 필드는 길이 제한이 없다
    # 하지만 인덱스에 넣을 수 없는 단점이 있다.
    # 인덱스에 넣지 못하는 이유 -> 인덱스는 메모리에 들어가는 balanced tree인데
    # 인덱스 -> 조회를 빠르게 하기 위한 자료구조 -> title 컬럼에 인덱스가 걸려있다 = title로 조회할 때 조회 성능이 빨라진다.
    # 길이 제한이 없는 값을 많이 넣는다면 메모리가 펑!

    class Meta:
        # 테이블 이름을 명시
        table = "articles"

    @classmethod
    async def get_one_by_id(cls, id: str) -> Article:
        # Article이 아직 완벽히 정의되지 않은 상태에서 Article을 다시 참조했으므로 에러가 난다.
        # 이 문제를 해결하기 위해서는 from __future__ import annotations를 해준다.
        # (참조 대신 type annotation을 처리하는 특수한 방법으로 선회하게 된다.)

        # 이처럼 Article을 쿼리하는 모든 함수를 Article 클래스 안에 두면 응집성이 높아진다.
        # 응집성이 높다 = Article과 관련된 모든 것이 Article 한 곳에 모여있어, 찾기가 쉬워진다.
        return await cls.get(id=id)
