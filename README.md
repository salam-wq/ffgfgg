# calc-ci-lab — учебный проект для ЛПР 12

Небольшой калькулятор на Python, на примере которого настраивается непрерывная
интеграция (CI) в **GitHub Actions** и **GitLab CI/CD**.

## Структура

```
.
├── .github/workflows/ci.yml   # workflow GitHub Actions
├── .gitlab-ci.yml             # pipeline GitLab CI/CD
├── pyproject.toml             # метаданные пакета и настройки pytest
├── requirements-dev.txt       # инструменты разработки (pytest, flake8, build)
├── .flake8                    # настройки линтера
├── src/calc/                  # исходный код пакета
│   ├── operations.py          # арифметические функции
│   └── cli.py                 # консольный интерфейс `calc`
└── tests/test_operations.py   # модульные тесты
```

## Локальный запуск

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate      Linux/macOS: source .venv/bin/activate
pip install -r requirements-dev.txt
flake8 src tests          # проверка кода
pytest -v                 # тесты
python -m build           # сборка: dist/*.whl и dist/*.tar.gz
pip install dist/*.whl && calc add 2 3
```

## Этапы CI

| Этап  | Что делает                                   | GitHub Actions (job) | GitLab CI (job) |
|-------|----------------------------------------------|----------------------|-----------------|
| lint  | `flake8 src tests`                           | `lint`               | `lint`          |
| test  | `pytest`, отчёт JUnit                        | `test`               | `test`          |
| build | `python -m build`, проверка установки wheel  | `build`              | `build`         |
