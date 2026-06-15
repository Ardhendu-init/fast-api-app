from motor.motor_asyncio import AsyncIOMotorClient
import os
import certifi

client = AsyncIOMotorClient(
    os.environ['MONGO_URI'],
    tls=True,
    tlsCAFile=certifi.where()
)

db = client["screening_test"]
users_collection = db["users"]