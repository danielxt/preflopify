from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import poker
import random
import rangeRFI
from rangeRFI import ALL_RFI_ACTIONS
from tableColorer import colorer

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



@app.get("/dealHand")
async def deal_hand() -> dict:
    chosenHand = random.choice(poker.hand.Range("XX").to_ascii().split())

    actionClass = random.choice(ALL_RFI_ACTIONS)
   
    chosenPosition = actionClass.position
    options = list(actionClass.optionToRange.keys())
    
    correctOption = actionClass.getCorrectAction(chosenHand)
    
    blankRangeTable = colorer([], [], [], chosenHand)
    
    coloredRangeTable = actionClass.getColoredTable(chosenHand)


    return {"hand": chosenHand, 
            "position": chosenPosition, 
            "options" : options, 
            "correctOption" : correctOption, 
            "blankRangeTable": blankRangeTable,
            "coloredRangeTable" : coloredRangeTable}