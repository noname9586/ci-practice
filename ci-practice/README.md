# ci-practice

Учебный проект для практической работы по настройке CI/CD-пайплайна в GitHub Actions.

## Состав проекта

- `app/validators.py` — функции проверки email, возраста и номера телефона.
- `tests/test_validators.py` — обычные модульные тесты.
- `tests/test_slow.py` — имитация медленных проверок.
- `tests/test_flaky.py` — нестабильный тест, вынесенный в карантин.
- `.github/workflows/ci.yml` — workflow GitHub Actions.
- `Dockerfile` — окружение для запуска тестов в контейнере.

## Запуск локально

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
pytest -v
ruff check .
```

Основной набор без карантинного теста:

```bash
pytest -m "not quarantine" -v
```

Карантин отдельно:

```bash
pytest -m quarantine -v
```

## Docker

```bash
docker build -t ci-practice-tests .
docker run --rm ci-practice-tests
```

## GitHub Actions

Загрузите проект в GitHub в репозиторий `ci-practice`. Workflow запускается при push и pull request в `main`.

В итоговом workflow тесты разделены на 4 части. Для замера без sharding временно замените job `unit` на один запуск `pytest -m "not quarantine" -v`. Для двух частей замените `shard: [1, 2, 3, 4]` на `shard: [1, 2]` и `--splits 4` на `--splits 2`.

Для задания с матрицей Python используйте версии `3.11` и `3.12` вместо матрицы `shard`.

## Важно

После первого запуска workflow откройте вкладку Actions и проверьте фактические результаты. Время выполнения, скриншоты, ссылку на репозиторий и ссылку на Issue нужно добавить в отчёт по результатам собственного запуска.
