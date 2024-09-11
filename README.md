# Memes App

## Functionality

- **GET /memes**: Retrieve a list of all memes.
- **GET /memes/{id}**: Retrieve a specific meme by its ID.
- **POST /memes**: Add a new meme.
- **PUT /memes/{id}**: Update an existing meme.
- **DELETE /memes/{id}**: Delete a meme.

- **GET /image/{id}**: Retrieve a specific meme image by its ID.
- **POST /image/{id}**: Add a new image for a meme.
- **PUT /image/{id}**: Update an existing meme image.
- **DELETE /image/{id}**: Delete a meme image.

## Installation and Launch

1. Install and launch the container:
   ```bash
   git clone https://github.com/StilUSoff/Mad_Soft_Task
   cd Mad_Soft_Task
   docker-compose up --build -d


2. API documentation is available at the following addresses:
   http://localhost:8000/api_docs
   http://localhost:8000/api_redoc
   http://localhost:8001/api_docs
   http://localhost:8001/api_redoc

3. MiniO Dashboard is available at:
   http://localhost:9001

## Testing
While in the Mad_Soft_Task folder, enter the following into the terminal:
1. To test the public API for working with the database:
   ```bash
   python tests/test_meme_api.py
   ```
2. To test the private API for working with the S3 storage:
   ```bash
   python tests/test_image_api.py
   ```
   You will need to enter the full path to the test image in the terminal:
   ```bash
   FILEPATH: E:\User\Pictures\test_image.jpg
   ```

## API Requests for Database

### GET
For the full list:
```bash
curl -X GET "http://localhost:8000/memes" -H "accept: application/json"
```
Or for a specific item:
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

## API Requests for S3

### GET FILE 
```bash
curl -X GET "http://localhost:8001/image/1?api_key=hDf6GVg8B0813klvs695HVlksd" -H "accept: application/json"
```
OR
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

deleting: 
docker rm -f $(docker ps -aq) \
docker rmi -f $(docker images -q) \
docker volume rm $(docker volume ls -q) \
docker builder prune -a -f 

enter container:
docker exec -it mad_soft_task-app-1 /bin/sh 
-->
