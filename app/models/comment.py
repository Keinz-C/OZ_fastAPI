from __future__ import annotations

from tortoise import Model, fields

from app.models.article import Article
from app.models.base_model import BaseModel


class Comment(BaseModel, Model):  # pydantic의 BaseModel을 import하지 않도록 주의
    article: fields.ForeignKeyRelation[Article] = fields.ForeignKeyField(
        model_name="models.Article",
        related_name="comment",
        db_constraint=False,
    )
    # fields.ForeignKeyRelation[Article는 타입
    # fields.ForeignKeyField(...)는 실제 값
    # 실제 db 테이블에는 article_id가 있다.

    author = fields.CharField(max_length=255)
    content = fields.TextField()

    class Meta:
        table = "comments"

    @classmethod
    async def get_all_by_article_id(cls, article_id: str) -> list[Comment]:
        """
        ## filter().all()...
        tortoise orm은 처음부터 설계 의도가 "Django ORM과 흡사하게"이다.
        django에 있었던 웬만한 것들은 tortoise orm에도 다 있다.
        django에

        """
        return await cls.filter(article_id=article_id).all()
