# 1일차 실습
## 1.  pycharm에서 서비 실행
<img width="852" alt="스크린샷 2024-10-30 오후 5 47 14" src="https://github.com/user-attachments/assets/c10666b5-c74a-4b9a-840a-78586f8dab0e">

## 2.  postman에서 "Hello World" 출력
<img width="1362" alt="스크린샷 2024-10-30 오후 6 01 52" src="https://github.com/user-attachments/assets/7b6e1ba5-7040-479b-b89c-a6db17c530b1">

## 3.  화면단 출력 확인
<img width="1792" alt="스크린샷 2024-10-30 오후 6 12 02" src="https://github.com/user-attachments/assets/1868baec-aeba-4499-857d-29b9bdbe3418">


# 1일차 필기
## 1. mypy 실행 시 클래스와 타입의 차이
- 클래스(class)
  ```
  class Copmputer():
    pass
  
  class DesktopComputer(Computer):
    pass
  ```
  - 여기서 DesktopComputer의 class는 DesktopComputer가 된다.
  - DesktopComputer의 클래스는 Computer가 될 수 없다.

- 타입(Type)
  - 위의 예시에서 Computer도 DesktopComputer도 DesktopComputer()의 타입이 될 수 있다.

- 정리
  - mypy시 "type[DesktopCopmputer]" has no attribute "속성"등 에러에 대한 간단한 이해
  - 메이플에서 나는 마법사다 -> type / 나는 마법사에서 힐러다 -> class
