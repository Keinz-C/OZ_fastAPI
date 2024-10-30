from tortoise import fields


class BaseModel:
    """
    앞으로 다른 모델들이 이 BaseModele을 상속받는다.

    상속 -> 멤버 변수와, 메소드를 물려준다.
    BaseModel은 메소드는 없고 멤버변수 3개만 있다.
    id, created_at, modified_at

    ## audit
    createde_at과 modified_at은 audit컬럼이다.
    audit은 "누가, 언제, 무엇을, 어떻게 수정했는가"를 기록으로 남기는 것을 audit이라고 한다.

    ## primary key는 big int를 사용한다.
    예전에는 primary key의 타입을 bigint로 했었다.
        -> 21억 건 이상의 데이터를 생성할 가능성이 있기에, int는 21억이 max라 공간이 부족하다.

    ## 어느 쪽이 큰가?
    bigint와 문자열(40)중에서는 문자열(40)이 더 크다
    -> 컬러의 크기가 크다는 것은 -> 성능은 반대로 떨어진다.

    ## 성능이 떨어짐에도 문자열을 사용하는 이유?
        -> 실전에서는 pk int 혹으 bigint를 쓰는게 맞긴하다

    """

    id = fields.CharField(pk=True, max_length=40)  # db와 통신할때 big int key로 통신
    # external_id = fields.CharField(pk=True, max_length=40) # 이게 더 안전함
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
