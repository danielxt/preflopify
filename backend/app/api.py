from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import poker
import random

app = FastAPI()

origins = [
    "http://localhost:5173",
    "localhost:5173"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/msg", tags=["msg"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}

@app.get("/getRandomHand")
async def read_root() -> dict:
    allhands = poker.hand.Range("XX").to_ascii().split()
    print(random.choice(allhands))
    return {"value": random.choice(allhands)}