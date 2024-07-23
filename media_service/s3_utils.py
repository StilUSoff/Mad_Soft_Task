import boto3
from botocore.client import Config
from botocore.exceptions import ClientError
from fastapi import UploadFile
import aiofiles
from fastapi.responses import StreamingResponse
from io import BytesIO

def get_s3_client():
    return boto3.client(
        's3',
        endpoint_url='http://minio:9000',
        aws_access_key_id='minio',
        aws_secret_access_key='minio123',
        config=Config(signature_version='s3v4')
    )

def create_bucket(s3_client, bucket_name):
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} already exists.")
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            s3_client.create_bucket(Bucket=bucket_name)
            print(f"Bucket {bucket_name} created successfully.")
        else:
            print(f"Failed to check or create bucket: {e}")
            raise

async def get_file(s3_client, bucket_name, file_key):
    response = s3_client.get_object(Bucket=bucket_name, Key=f'{file_key}.jpg')
    file_stream = BytesIO(response['Body'].read())
    return StreamingResponse(file_stream, media_type="image/jpeg")


async def upload_file_to_s3(s3_client, bucket_name, meme_id, file: UploadFile):
    async with aiofiles.open(file.filename, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)

    s3_client.upload_file(
        Filename=file.filename,
        Bucket=bucket_name,
        Key=f'{str(meme_id)}.jpg'
    )
    file_url = f"http://localhost:9000/{bucket_name}/{meme_id}.jpg'"
    return file_url

async def update_file_in_s3(s3_client, bucket_name, meme_id, file: UploadFile):
    async with aiofiles.open(file.filename, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)

    # Загрузка файла в S3
    s3_client.upload_file(
        Filename=file.filename,
        Bucket=bucket_name,
        Key=f'{str(meme_id)}.jpg'
    )
    # Генерация URL для доступа к файлу
    file_url = f"http://localhost:9000/{bucket_name}/{meme_id}.jpg'"
    return file_url

async def delete_file_from_s3(s3_client, bucket_name, meme_id):
    s3_client.delete_object(
            Bucket=bucket_name,
            Key=f'{str(meme_id)}.jpg'
        )