![tests passed](https://github.com/molspace/nfactorial_python_dev/hw_backend2/users/users_tests.png)

# users

Данная папка предназначена для следующих заданий:
- users-all
- users-id
- users-pagination 💎

> 💡 Необходимо чтобы задания были выполнены в данной папке.

## Запуск проекта

Установить зависимости:

```bash
poetry install
```

Войти в окружение poetry:

```bash
poetry shell
```

Запустить FastAPI-приложение.

```bash
uvicorn app.main:app --reload
```

После этого сервер запуститься на порту 8000. Чтобы проверить подключение сделайте запрос на [localhost:8000](http://localhost:8000).

```bash
curl localhost:8000
```

Запустить тесты.

```bash
pytest -v
```
