from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from app.configs import settings

TORTOISE_APP_MODELS = [
    "app.models.article",
    "app.models.comment",
    "aerich.models",
]

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",  # 어떤 driver를 사용할 거이냐
            # orm은 database랑 직접 소통하는 것이 아닌 driver을 통해서 소통한다.
            # 대표적인 postgres용 driver : psycopg2
            # mysql + tortoise랑 자주 같이 사요하는 driver가 asyncmy
            # 이렇게 각종 drvier로 수많은 다른 데이터베이스에 접근할 수 있다.
            "credentials": {
                "host": settings.DB_HOST,
                "port": settings.DB_PORT,
                "user": settings.DB_USER,
                "password": settings.DB_PASSWORD,
                "database": settings.DB_DB,
                "connect_timeout": 5,
                # "maxsize": configs.MAX_CONNECTION_PER_CONNECTION_POOL,    # 찾아봐 ㅋ
            },
        },
    },
    "apps": {
        "models": {
            "models": TORTOISE_APP_MODELS,
        },
    },
    # 실전에서는 master 데이터베이스 (쓰기를 담당한다.) 하나와
    # 다수의 replica (읽기만 담당)로 구성된다.
    # 사용자가 쓰기를 연산하ㅡㄴ지, 읽기 연산을 하는지에 따라서 라우팅을 할 필요가 있다.
    # 서비스가 커짐에 따라, 상황에 따라서 데이터베이스를 골라주는 역할을 하는게 router이다.
    # "routers": ["app.configs.database_config.Router"],    # 찾아봐 ㅋ
    "timezone": "Asia/Seoul",
}


def initialize(app: FastAPI) -> None:
    Tortoise.init_models(TORTOISE_APP_MODELS, "models")
    register_tortoise(app, config=TORTOISE_ORM)
