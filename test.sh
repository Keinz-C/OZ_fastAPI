set -eo pipefail

COLOR_GREEN=`tput setof 2;`
COLOR_NC=`tput sgr0;` # No Color

echo "Starting black"
poetry run black .

echo "Starting isort"
poetry run isort .

echo "Starting mypy"
poetry run mypy .

echo "Starting pytest with coverage"
poetry run coverage run -m pytest   # coverage를 측정하면서 "pytest"를 실행할 것이다.
poetry run coverage report -m       # 테스트 종료 후, coverage가 어떻게 되는지 조회
poetry run coverage html

echo "${COLOR_GREEN}All tests passed successfully!${COLOR_NC}"