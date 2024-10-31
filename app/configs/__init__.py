from app.configs.base_settings import Settings


def get_settings() -> Settings:
    """
    1. pydantic은 기본적으로 (default 설정) "환경 변수"에서 설정값을 읽는다.
    2. env_file을 전달한다면 .env를 읽는다.

    env_file과 환경 변수중에서는 항상 환경 변수가 우선된다.
        -> 환경변수에 MY_NAME=name라고 되어있고, env_file에 MY_NAME=name이라고 되어있다면
            -> 환겨변수가 우선되므로 MY_NAME은 첫 번째 name이 된다.

    # error에서 Unexpected keyword argument란?
      # 우선 파이선은 함수에 전달하는 인수(인자)는 아래로 나뉜다.
        - keyword argument : 키워드 매개변수 - 이름으로 매개변수를 전달한다. 위치와 상관없이 원하는 값을 전달할 수 있음.
        - positional argument : 위치 매개변수 - 말 그대로 매개변수의 순서에 맞춰서 값을 전달한다.

    """
    return Settings(_env_file=".env", _env_file_encoding="utf-8")


settings = get_settings()
