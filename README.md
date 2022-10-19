# Запуск
Если запускать `pipenv run uvicorn asgi:app` все ок!
Если попробовать `pipenv run gunicorn asgi:app -k uvicorn.workers.UvicornWorker --access-logfile -` то консьюмер не заводится.

Создается 2 ендпоинта
- Flask `http://127.0.0.1:8000/v1`
- FastApi `http://127.0.0.1:8000/`

# TODO
- Запустить `standalone` через `gunicorn`
- Создать выбор типа запуска через `ENV` переменную
