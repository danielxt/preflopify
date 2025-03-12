import poker
import random
from actionClass import ActionClass
    

UTG_RFI = ActionClass("Lojack", 
                      {"Raise": poker.hand.Range("A2s+ ATo+ KJo+ 44+ QJs+ JTs+ T9s+ 98s 87s 76s 65s K9s+ Q9s+ J9s+").to_ascii().split()})

UTG1_RFI = ActionClass("Hijack",
                        {"Raise": poker.hand.Range("A2s+ ATo+ KJo+ QJo+ K8s+ Q9s+ J9s+ T8s+ 97s+ 87s 76s 65s 54s 22+").to_ascii().split()})

CUTOFF_RFI = ActionClass("Cutoff", 
                          {"Raise" : poker.hand.Range("A9o+ KTo+ QTo+ 22+ A2s+ K7s+ Q8s+ J8s+ T8s+ 97s+ 86s+ 75s+ 64s+ 54s 43s").to_ascii().split()})

BUTTON_RFI = ActionClass("Button",
                          {"Raise" : poker.hand.Range("A2o+ A2s+ K2s+ Q2s+ J6s+ T6s+ 96s+ 86s+ 85s+ K7o+ Q8o+ J8o+ T8o+ 97o+ 87o+ 76o+ 74s+ 64s+ 53s+ 43s+ 32s+ 22+").to_ascii().split()})



ALL_RFI_ACTIONS = [UTG_RFI, UTG1_RFI, CUTOFF_RFI, BUTTON_RFI]






    
