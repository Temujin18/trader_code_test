from fastapi import APIRouter, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from .models import Order

router = APIRouter()


@router.get("/")
def index():
    return {"detail": "Welcome to Simple Trader API!"}


async def get_order_by_id(collection, file_id: int):
    return await collection.find_one({"_id": file_id}, {"_id": False})


def get_portfolio_by_user_id(collection, user_id: int):
    return collection.find({"user_id": user_id}, {"_id": False, "user_id": False})


@router.post("/api/")
async def post_order(request: Request, post_data: Order):
    mongo_collection = request.app.mongodb[Order.__collection_name__]
    data = post_data.dict()
    created_file = await mongo_collection.insert_one(data)
    response = await get_order_by_id(mongo_collection, file_id=created_file.inserted_id)

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonable_encoder(response))


@router.get("/api/portfolio/{user_id}")
async def get_user_portfolio(request: Request, user_id: int):
    collection = request.app.mongodb[Order.__collection_name__]
    orders = get_portfolio_by_user_id(collection, user_id)

    response = []
    async for order in orders:
        response.append(order)

    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(response))


