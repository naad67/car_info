# http://127.0.0.1:8080/docs

 - Запуск проекта с базой данных
```shell
docker-compose -f docker-compose.yml up -d --build
```

 - Создание табилицы cars
```shell
docker-compose -f docker-compose.yml exec api alembic upgrade head 
```

 - Запустить скрипт с тестовами данными 
```shell
docker-compose -f docker-compose.yml exec api python initial.py
```
