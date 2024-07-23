# Memes App

## Функциональность

- **GET /memes**: Получить список всех мемов.
- **GET /memes/{id}**: Получить конкретный мем по его ID.
- **POST /memes**: Добавить новый мем.
- **PUT /memes/{id}**: Обновить существующий мем.
- **DELETE /memes/{id}**: Удалить мем.

- **GET /image/{id}**: Получить конкретное изображение мема по его ID.
- **POST /image/{id}**: Добавить новое изображение для мема.
- **PUT /image/{id}**: Обновить существующее изображение мема.
- **DELETE /image/{id}**: Удалить изображение мема.

## Установка и запуск

1. Установка и запуск контейнера:
   ```bash
   git clone https://github.com/StilUSoff/Mad_Soft_Task
   cd Mad_Soft_Task
   docker-compose up --build -d
   ```

2. Ссылка с документацией API лежит по адресам:
   http://localhost:8000/api_docs
   http://localhost:8000/api_redoc
   http://localhost:8001/api_docs
   http://localhost:8001/api_redoc

3. Личный кабинет MiniO лежит по адресу:
   http://localhost:9001

## Тестирование

Находясь в папке Mad_Soft_Task введите в терминал:  
1. Для тестирования открытого API для работы с БД:
   ```bash
   python tests/test_meme_api.py
   ```
2. Для тестирования закрытого API для работы с S3-хранилищем:
   ```bash
   python tests/test_image_api.py
   ```
   Нужно будет ввести в терминал полный путь к тестовому изображению:
   ```bash
   FILEPATH: E:\User\Pictures\test_image.jpg
   ```

## Запросы к API с базой данных

### GET
Для полного списка:
```bash
curl -X GET "http://localhost:8000/memes" -H "accept: application/json"
```
Или для конкретного элемента:
```bash
curl -X GET "http://localhost:8000/memes/1" -H "accept: application/json"
```
### POST

```bash
curl -X POST "http://localhost:8000/memes" -H "accept: application/json" -H "Content-Type: application/json" -d '{"title": "New Meme", "image_url": "http://example.com/image.jpg"}'
```
Или
```bash
Invoke-RestMethod -Uri "http://localhost:8000/memes" -Method Post -Headers @{ "accept" = "application/json"; "Content-Type" = "application/json" } -Body '{ "title": "New Meme"}'
```

### PUT
```bash
curl -X PUT "http://localhost:8000/memes/1" -H "accept: application/json" -H "Content-Type: application/json" -d '{"title": "Updated Meme"}'
```

Или
```bash
Invoke-RestMethod -Uri "http://localhost:8000/memes/1" -Method Put -Headers @{ "accept" = "application/json"; "Content-Type" = "application/json" } -Body '{ "title": "Updated Meme"}'
```

### DELETE
```bash
curl -X DELETE "http://localhost:8000/memes/1" -H "accept: application/json"
```

## Запросы к API с S3

### GET FILE 
```bash
curl -X GET "http://localhost:8001/image/1?api_key=hDf6GVg8B0813klvs695HVlksd" -H "accept: application/json"
```
ИЛИ
```bash
curl -X GET "http://localhost:8001/image/1?api_key=hDf6GVg8B0813klvs695HVlksd" -H "accept: application/json" --output C:\Downloads\file.jpg
```

### POST FILE 
```bash
curl -X POST "http://localhost:8001/image/1?api_key=hDf6GVg8B0813klvs695HVlksd" -H "accept: application/json" -F "file=@path_to_your_image.jpg"
```

### PUT FILE 
```bash
curl -X PUT "http://localhost:8001/image/1?api_key=hDf6GVg8B0813klvs695HVlksd" -H "accept: application/json" -F "file=@path_to_your_image.jpg"
```

### DELETE FILE 
```bash
curl -X DELETE "http://localhost:8001/image/1?api_key=hDf6GVg8B0813klvs695HVlksd" -H "accept: application/json" -F 
```

<!-- 
docker ps   
docker stop $(docker ps -q)
docker-compose run app sh
docker-compose run media_service sh
docker-compose build --no-cache
docker-compose up -d
docker-compose up --build -d

удаление: 
docker rm -f $(docker ps -aq) \
docker rmi -f $(docker images -q) \
docker volume rm $(docker volume ls -q) \
docker builder prune -a -f 

вход в контейнер:
docker exec -it mad_soft_task-app-1 /bin/sh 
-->