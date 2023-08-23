from fastapi import FastAPI
from typing import List
from models.forms import User, Trade

app = FastAPI()

fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "Tom"},
    {"id": 3, "role": "trader", "name": "Mat"},
    {"id": 4, "role": "investor", "name": "Homer", "degree": [
        {"id": 1, "created_at": "2020-01-01T00:00:00", "type_degree": "expert"}
    ]},
]

fake_trades = [
    {"id": 1, "usser_id": 1, "currency": "BTC",
        "side": "buy", "price": 123, "amount": 1.2},
    {"id": 2, "usser_id": 1, "currency": "BTC",
        "side": "sell", "price": 234, "amount": 2.2},
]


@app.get("/")
def index():
    return "Hello world"


@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]


@app.post("/trades")
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}
