from tortoise.contrib.test import TestCase

from app.models.article import Article
from app.services.article_service import service_get_article_and_comments

# django랑 똑같은 TestCase를 import 해서 애용한다.
# tortoise orm에서 가져옴


class TestArticleService(TestCase):

    async def test_get_article_and_comment(self) -> None:
        """
        := -> wallus operator (바다코끼리연산자)


        """
        # Given
        # test에 필요한 재료 준비
        # 게시글을 제대로 조회 가능한지 검사
        article_id = "test_article"
        article = await Article.create(
            id=article_id, author=(author := "author"), title="title", body="body"
        )

        # When
        # Call to untyped function "service_get_article_and_comments" in typed context
        # type이 다 되어 있는 문맥 속에서, 타입이 없는 함수를 호출한 에러
        article_and_comment = await service_get_article_and_comments(article_id)

        # Then
        self.assertEqual(article_and_comment.id, article_id)
        self.assertEqual(article_and_comment.author, author)
        self.assertEqual(article_and_comment.title, "title")
        self.assertEqual(article_and_comment.body, "body")
