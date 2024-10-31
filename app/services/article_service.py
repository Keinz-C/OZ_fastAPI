from app.dtos.article_and_comments_response import (ArticleAndCommentsResponse,
                                                    CommentResponse)
from app.models.article import Article
from app.models.comment import Comment


async def service_get_article_and_comments(
    article_id: str,
) -> ArticleAndCommentsResponse:
    """

    await:
        - 비동기 호출을 한다. (async def로 시작하는 함수를 호출)
        - 이벤트 루프에게 이 함수를 호출해 달라고 등록한다.
        - 내가 등록한 함수가 호출 완료되기까지 기다린다.
            - 만약 db 호출이라면 결과가 돌아올 때까지 기다리는 것을 의미한다.

    이벤트 루프
        - 여러가지 비동기 함수들을 대신 실행해 준다.
        - 무한 루프 : 영원히 반복되는 while문과 비슷함

    """
    article = await Article.get_one_by_id(article_id)
    comments = await Comment.get_all_by_article_id(article_id)

    return ArticleAndCommentsResponse(
        id=article.id,
        author=article.author,
        title=article.title,
        body=article.body,
        comments=tuple(
            CommentResponse(id=comment.id, author=comment.author, body=comment.content)
            for comment in comments
        ),
    )
