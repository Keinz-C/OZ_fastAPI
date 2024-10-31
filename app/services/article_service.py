import asyncio

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

    비동기란?
        - 외부 IO 요청을 한 뒤에 내가 딴 짓을 할 수 있나?
        - django IO 요청 후에 아무것도 못하고 block 되면 동기6

    parallel과 concurrent의 차이 / 병렬 처리의 차이
        - 은행가서 통장 만들고, 치킨집에서 치킨사고, 마트에서 우유사는 task가존재
        - 3개의 task가 존재한다면

            parallel의 경우: (동기)
                - 사람 3명이 각각의 일을 실행함
                - 사람 1명이 은행, 1명은 치킨집, 1명은 마트를 간다

            concurrent의 경우: (비동기)
                - 사람 1명이 각각의 일을 실행함
                - 은행가서 번호표 뽑고, 치킨가서 주문하고, 마트가서 우유사고, 치킨집에서 포장하고, 은행가서 통장만듦

        - 더 적은 자원으로 여러 개의 task를 수행할 수 있는 것 = concurrent
        - 다만, 한 군데에서 걸리면 다른 task 수행에 차질이 생긴다.

        - parallel은 사람 3명이 각각 일을 하기 때문에 각 task에 영향을 끼치지 않는다.
        = 사람 -> cpu core와 같음 (혹은 process를 의미하기도 한다.)
        - task는 IO 요청을 말한다.(데이터베이스 호출, http 호출)
        - 은행, 치킨집, 마트 등은 IO요청을 받아들이는 주체 (데이터베이스, 외부 서버)

    asyncio.gether():
        - 비동기 호출을 "동시적(Concurrent)"하게 진행하는 2가지 방법중 하나이다.
        - gather(), as_completed()가 있다.
        - gather()를 호출할 때는 다수의 코루틴을 전달한다.
        - 모든 코루틴을 실행 완료되었을 때까지 대기한 후, 다되었다면 순서대로 반환한다.

    """
    article, comments = await asyncio.gather(
        Article.get_one_by_id(article_id),  # 1번 인자 먼저 반환(article로)
        Comment.get_all_by_article_id(article_id),  # 2번 인자 다음 반환(comments로)
    )

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
