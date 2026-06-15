from pymongo import MongoClient
from dotenv import load_dotenv
import os
import certifi

load_dotenv()

uri = os.getenv("MONGO_URI")

print("Using cert bundle:", certifi.where())

client = MongoClient(
    uri,
    tls=True,
    tlsCAFile=certifi.where()
)

try:
    result = client.admin.command("ping")
    print("✅ Connected!")
    print(result)
except Exception as e:
    print("❌ Failed")
    print(type(e).__name__)
    print(e)