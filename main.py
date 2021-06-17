from fastapi import FastAPI
import uvicorn

from motor.motor_asyncio import AsyncIOMotorClient
from api.trader_api_routes import router

app = FastAPI()


@app.on_event("startup")
async def init_db_client():
    app.mongodb_client = AsyncIOMotorClient()
    app.mongodb = app.mongodb_client["Trader_Api"]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app=app, debug=True)
