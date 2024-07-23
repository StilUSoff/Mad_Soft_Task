from fastapi import FastAPI, File, Depends, UploadFile, HTTPException
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from media_service.s3_utils import get_s3_client, create_bucket, upload_file_to_s3, update_file_in_s3, delete_file_from_s3, get_file

app = FastAPI(docs_url="/api_docs", redoc_url="/api_redoc")
s3_client = get_s3_client()
bucket_name = "memes"

def verify_api_key(api_key: str):
    if api_key != "hDf6GVg8B0813klvs695HVlksd":
        raise HTTPException(status_code=403, detail="Unauthorized")

@app.on_event("startup")
def startup_event():
    create_bucket(s3_client, bucket_name)

@app.get("/image/{meme_id}")
async def see_file(meme_id: int, api_key: str = Depends(verify_api_key)):
    try:
        url = await get_file(s3_client,bucket_name, meme_id)
        return url
    except (NoCredentialsError, PartialCredentialsError):
        raise HTTPException(status_code=400, detail="S3 credentials are invalid")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/image/{meme_id}")
async def upload_file(meme_id: int, api_key: str = Depends(verify_api_key), file: UploadFile = File(...)):
    try:
        file_url = await upload_file_to_s3(s3_client, bucket_name, meme_id, file)
        return {"file_url": file_url}
    except (NoCredentialsError, PartialCredentialsError):
        raise HTTPException(status_code=400, detail="S3 credentials are invalid")
    
@app.put("/image/{meme_id}")
async def update_file(meme_id: int, api_key: str = Depends(verify_api_key), file: UploadFile = File(...)):
    try:
        file_url = await update_file_in_s3(s3_client, bucket_name, meme_id, file)
        return {"file_url": file_url}
    except (NoCredentialsError, PartialCredentialsError):
        raise HTTPException(status_code=400, detail="S3 credentials are invalid")
    
@app.delete("/image/{meme_id}")
async def delete_file(meme_id: int, api_key: str = Depends(verify_api_key)):
    try:
        delete_file_from_s3(s3_client, bucket_name, meme_id)
        return {"Success!"}
    except (NoCredentialsError, PartialCredentialsError):
        raise HTTPException(status_code=400, detail="S3 credentials are invalid")
    except s3_client.exceptions.ClientError as e:
        if e.response['Error']['Code'] == '404':
            raise HTTPException(status_code=404, detail="File not found")
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
