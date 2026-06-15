from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

app = FastAPI()



app.include_router(router)


@app.get("/")
async def root():
    return {"message": "API Working"}






