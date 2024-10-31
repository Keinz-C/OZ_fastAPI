from enum import StrEnum

from pydantic_settings import BaseSettings


class Env(StrEnum):
    """
    enum을 만드는 이유 : 자동 완성과 타입 체킹
    -> 오타 등 실수했을 때 IDE가 잡아줄 수 있다.

    Mypy error ex:
    app/configs/base_settings.py:18: error: "type[Env]" has no attribute "LOCAe"  [attr-defined]
    Found 1 error in 1 file (checked 6 source files)

    type[Env]에는 LOCAe라는 속성(attribute)가 없다.

    속성이란?
    -> .(dot : 접근 연산자) 연산자로 접근 해 봤을 때, Env 안에는 "LOCAe"가 없다.

    type = class이다.(이거로 이해만 해놔라)
    """

    LOCAL = "local"  # locla : 개발자가 개발하는 곳
    STAGE = "stage"  # stage : QA와 함께 배포전 정상동작 확인하는 곳
    PROD = "prod"  # production : 실제 배포되는 곳. 진짜 서버


class Settings(BaseSettings):
    ENV: Env = Env.LOCAL
    DB_HOST: str = "127.0.0.1"  # localhost랑 같은 의미
    DB_PORT: int = 3306
    DB_USER: str = "root"  # mysql 기본 계정
    DB_PASSWORD: str = "1685"
    DB_DB: str = "oz_festapi_5"
