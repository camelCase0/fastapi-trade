from auth.database import User
from auth.manager import get_user_manager
from auth.auth import auth_backend
from auth.schema import UserCreate, UserRead
from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from typing import List
# from models.forms import User, Trade

app = FastAPI(title="Trading app")

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

# @app.get("/")
# def index():
#     return "Hello world"


# @app.get("/users/{user_id}", response_model=List[User])
# def get_user(user_id: int):
#     return [user for user in fake_users if user.get("id") == user_id]


# @app.post("/trades")
# def add_trades(trades: List[Trade]):
#     fake_trades.extend(trades)
#     return {"status": 200, "data": fake_trades}
