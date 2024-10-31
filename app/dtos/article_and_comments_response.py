from pydantic import BaseModel


class CommentResponse(BaseModel):
    """
    Reasponse dto를 생성
    response dto는 결과 json에 어떤 값이 들어갈지 결정한다.
    댓글이 가지고 있는 많은 컬럼들 중에서
    - 댓글의 id
    - 댓글의 작성자
    - 댓글의 본문
    위 3개의 컬럼을 클라이언트에게 전달

    fastapi는 response dto를 보고
    response spec을 자동으로 생성(자동으로 swagger가 만들어짐)
    """

    id: str
    author: str
    body: str


class ArticleAndCommentsResponse(BaseModel):
    """
    게시글과 댓글을 모두 담는 dto를 생성

    dto -> Data Transger Object -> 정보를 담고 있는 객체
    -> 정보를 수정한다면 dto가 아니다. 담고만 있어야 dto이다.

    fastapi에서 dto는 보통 pydantic의 BaseModel을 상속하는 모델을 만든다.

    함수가 dict를 리턴하도록 하지 말 것(99.9% 상황에서는 dict 대신 dto를 사용할 수 있다.)

    don't:
        return {"abc": "def}

    do:
        return MyDto(abc="def")
    """

    # 게시글의 id, 작성자, 제목, 본문, 댓글목록을 정보로 담고있음
    id: str
    author: str
    title: str
    body: str
    # 일부러 list 대신 tuple을 사용
    # list의 type annotation을 작성할 때에는 list[CommentResponse] 이렇게 했을 것이지만,
    # tuple의 경우는 type annotation이 "길이"도 지정한다.
    # 길이를 모르는 경우 아래와 같이 ", ..."을 사용
    # 의미는, CommentResponse가 담긴 튜플인데, 길이가 가변적이다.

    # 리스트 대신 튜플을 쓰는 이유 -> 튜플은 immutable(불변)하다.
    # immutable -> 생성 후 불변
    # 불변 -> 예측 가능성이 높다 -> 가독성이 좋다.
    comments: tuple[CommentResponse, ...]
