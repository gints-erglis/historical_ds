import os
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from minio import Minio

app = FastAPI()

# Use environment variables for DB connection
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://admin:password@localhost/historical_data")
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Configure MinIO using environment variables
MINIO_CLIENT = Minio(
    os.getenv("MINIO_ENDPOINT", "localhost:9000").replace("http://", ""),
    access_key=os.getenv("MINIO_ACCESS_KEY", "minioadmin"),
    secret_key=os.getenv("MINIO_SECRET_KEY", "minioadmin"),
    secure=False,
)

BUCKET_NAME = os.getenv("BUCKET_NAME", "historical-files")
if not MINIO_CLIENT.bucket_exists(BUCKET_NAME):
    MINIO_CLIENT.make_bucket(BUCKET_NAME)

@app.get("/")
async def root():
    return {"message": "Historical Data Storage API is running!"}
