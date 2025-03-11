from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import poker
import random
import rangeRFI
from rangeRFI import utg, utg1, cutoff, button, smallBlind

app = FastAPI()

RFI_POSITION_TO_RANGE = {
    "UTG" : utg,
    "UTG+1" : utg1,
    "Cutoff" : cutoff,
    "Button" : button,
    # "Small Blind" : smallBlind
}

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


@app.get("/dealHand")
async def deal_hand() -> dict:
    chosenHand = random.choice(poker.hand.Range("XX").to_ascii().split())

    chosenPosition = random.choice(list(RFI_POSITION_TO_RANGE.keys()))
    options = ["fold", "raise"]
    correctOption = ""
    if chosenHand in RFI_POSITION_TO_RANGE[chosenPosition].to_ascii().split():
        correctOption = "raise"
    else:
        correctOption = "fold"
    
    return {"hand": chosenHand, "position": chosenPosition, "options" : options, "correctOption" : correctOption, 
            "rangeTable": RFI_POSITION_TO_RANGE[chosenPosition].to_html()}