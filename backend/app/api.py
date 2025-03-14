from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import poker
import random
import rangeRFI
from rangeRFI import ALL_RFI_ACTIONS
from range3Bet import ALL_3BET_ACTIONS
from rangeFacingRFI import ALL_FACING_RFI_ACTIONS
from tableColorer import colorer

app = FastAPI()


SCENARIOS = {
    "Raise First In" : ALL_RFI_ACTIONS,
    "Facing 3bet" : ALL_3BET_ACTIONS,
    "Facing Raise First In" : ALL_FACING_RFI_ACTIONS
}

origins = [
    "http://localhost:5173",
    "localhost:5173",
    "https://main.d2ubsh4n62h2f3.amplifyapp.com/"
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
    
    chosenScenario = random.choice(list(SCENARIOS.keys()))

    actionClass = random.choice(SCENARIOS[chosenScenario])
   
    chosenPosition = actionClass.position
    options = list(actionClass.optionToRange.keys())
    
    correctOption = actionClass.getCorrectAction(chosenHand)
    
    blankRangeTable = colorer([], [], [], chosenHand, "", "", "")
    
    coloredRangeTable = actionClass.getColoredTable(chosenHand)


    return {"hand": chosenHand, 
            "position": chosenPosition, 
            "options" : options, 
            "scenario" : chosenScenario,
            "correctOption" : correctOption, 
            "blankRangeTable": blankRangeTable,
            "coloredRangeTable" : coloredRangeTable}