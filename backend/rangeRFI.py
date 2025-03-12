import poker
import random
from actionClass import ActionClass
    

LJ_RFI = ActionClass("Lojack", 
                      {"Raise": poker.hand.Range("A2s+ ATo+ KJo+ 44+ QJs+ JTs+ T9s+ 98s 87s 76s 65s K9s+ Q9s+ J9s+").to_ascii().split()})

HJ_RFI = ActionClass("Hijack",
                        {"Raise": poker.hand.Range("A2s+ ATo+ KJo+ QJo+ K8s+ Q9s+ J9s+ T8s+ 97s+ 87s 76s 65s 54s 22+").to_ascii().split()})

CUTOFF_RFI = ActionClass("Cutoff", 
                          {"Raise" : poker.hand.Range("A9o+ KTo+ QTo+ 22+ A2s+ K7s+ Q8s+ J8s+ T8s+ 97s+ 86s+ 75s+ 64s+ 54s 43s").to_ascii().split()})

BUTTON_RFI = ActionClass("Button",
                          {"Raise" : poker.hand.Range("A2o+ A2s+ K2s+ Q2s+ J6s+ T6s+ 96s+ 86s+ 85s+ K7o+ Q8o+ J8o+ T8o+ 97o+ 87o+ 76o+ 74s+ 64s+ 53s+ 43s+ 32s+ 22+").to_ascii().split()})

SMALL_BLIND_RFI = ActionClass("Small Blind",
                              {"Raise for Value" : poker.hand.Range("88-QQ ATo-AQo ATs-AKs KJs-KQs QJs KQo KJo").to_ascii().split(),
                               "Raise as a Bluff" : poker.hand.Range("J2s-J4s T4s T5s 94s 95s 84s 85s 74s 63s 53s 43s K2o-K3o Q2o-Q5o J6o T6o 96o 86o").to_ascii().split(),
                               "Limp" : poker.hand.Range("KK+ AKo A2o-A9o K4o-KTo Q6o-QJo J7o-JTo T7o-T9o 97o-98o 87o A2s-A9s K2s-KTs Q2s-QTs J5s-JTs T6s-T9s 96s-98s 86s-87s 75s-76s 64s 65s 54s 32s 22-77").to_ascii().split(),
                               
                               
                               })




ALL_RFI_ACTIONS = [LJ_RFI, HJ_RFI, CUTOFF_RFI, BUTTON_RFI, SMALL_BLIND_RFI]






    
