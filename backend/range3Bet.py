from actionClass import ActionClass

# LJ
LJ_VS_HJ_3BET = ActionClass("LJ vs HJ 3Bet", 
                      {"4-bet for Value": "AA AKs AKo KK QQ".split(),
                       "4-bet as a Bluff" : "A9s A8s A5s A4s A3s A2s KQo AJo".split(),
                       "Call" : "AQs AJs ATs KQs KJs KTs AQo QJs QTs JJ JTs TT T9s 99 98s 88 77".split()
                       })
LJ_VS_CO_3BET = ActionClass("LJ vs CO 3Bet", {"4-bet for Value": "AA AKs AKo KK QQ JJ".split(),
                       "4-bet as a Bluff" : "A9s A8s A5s A4s A3s A2s KQo AJo".split(),
                       "Call" : "AQs AJs ATs KQs KJs KTs AQo QJs QTs JTs TT T9s 99 98s 88 77 66".split()
                       })


LJ_VS_BTN_3BET = ActionClass("LJ vs BTN 3Bet", {"4-bet for Value": "AA AKs AKo KK QQ JJ".split(),
                       "4-bet as a Bluff" : "A9s A8s A7s A5s A5s A4s A3s A2s KQo AJo 76s".split(),
                       "Call" : "AQs AJs ATs KQs KJs KTs AQo QJs QTs JTs TT T9s 99 98s 88 87s 77 66 55".split()
                       })

LJ_VS_SB_3BET = ActionClass("LJ vs SB 3Bet", {"4-bet for Value": "AA AKs AKo KK QQ JJ".split(),
                       "4-bet as a Bluff" : "A9s A8s A7s A6s A5s A4s A3s A2s ATo KJo".split(),
                       "Call" : "AQs AJs ATs KQs KJs KTs AQo KQo QJs QTs AJo JTs J9s TT T9s 99 98s 88 87s 77 76s 66 55".split()
                       })

LJ_VS_BB_3BET = ActionClass("LJ vs BB 3Bet", {"4-bet for Value": "AA AKs AKo KK QQ JJ".split(),
                       "4-bet as a Bluff" : "A9s A8s A7s A6s A5s A4s A3s A2s AJo KQo".split(),
                       "Call" : "AQs AJs ATs KQs KJs KTs AQo QJs QTs JTs TT T9s 99 98s 88 87s 77 76s 66 55 44".split()
                       })

# HJ

HJ_VS_CO_3BET = ActionClass("HJ vs CO 3Bet", {"4-bet for Value": "AA AKs AKo KK QQ JJ".split(),
                       "4-bet as a Bluff" : "A9s A8s A7s A6s A5s A4s A3s A2s KJo ATo 76s".split(),
                       "Call" : "AQs AJs ATs KQs KJs KTs K9s AQo KQo QJs QTs Q9s AJo JTs J9s TT T9s 99 98s 88 87s 77 66 55".split()
                       })

HJ_VS_BTN_3BET = ActionClass("HJ vs BTN 3Bet", {"4-bet for Value": "AA AKs AKo KK QQ JJ".split(),
                       "4-bet as a Bluff" : "A9s A8s A7s A6s A5s A4s A3s A2s KJo ATo 76s 65s 54s".split(),
                       "Call" : "AQs AJs ATs KQs KJs KTs K9s AQo KQo QJs QTs Q9s AJo JTs J9s TT T9s 99 98s 88 87s 77 66 55 44".split()
                       })

HJ_VS_SB_3BET = ActionClass("HJ vs SB 3Bet", {"4-bet for Value": "AA AKs AKo KK QQ JJ".split(),
                       "4-bet as a Bluff" : "A9s A8s A7s A6s A5s A4s A3s A2s KJo ATo".split(),
                       "Call" : "AQs AJs ATs KQs KJs KTs K9s AQo KQo QJs QTs Q9s AJo JTs J9s TT T9s 99 98s 88 87s 77 76s 66 55 44".split()
                       })

HJ_VS_BB_3BET = ActionClass("HJ vs SB 3Bet", {"4-bet for Value": "AA AKs AKo KK QQ JJ".split(),
                       "4-bet as a Bluff" : "A9s A8s A7s A6s A5s A4s A3s A2s KQo AJo".split(),
                       "Call" : "AQs AJs ATs KQs KJs KTs AQo QJs QTs JTs TT T9s 99 98s 88 87s 77 76s 66 55 44".split()
                       })

# CO

CO_VS_BTN_SB_3BET = ActionClass("CO vs BTN/SB 3Bet", {"4-bet for Value": "AA AKs AKo KK QQ JJ TT".split(),
                       "4-bet as a Bluff" : "A8s A7s A6s A4s A3s A2s KJo ATo 97s 86s 75s 54s".split(),
                       "Call" : "AQs AJs ATs A9s A5s KQs KJs KTs K9s AQo KQo QJs QTs Q9s AJo JTs J9s T9s T8s 99 98s 88 87s 77 76s 66 65s 55 44".split()
                       })

CO_VS_BB_3BET = ActionClass("CO vs BB 3Bet", {"4-bet for Value": "AA AKs AKo KK QQ JJ TT".split(),
                       "4-bet as a Bluff" : "A8s A4s A3s A2s KJo ATo T8s 97s 65s 54s".split(),
                       "Call" : "AQs AJs ATs A9s A5s KQs KJs KTs K9s AQo KQo QJs QTs Q9s AJo JTs J9s T9s 99 98s 88 87s 77 76s 66 55 44".split()
                       })

# BTN
BTN_VS_SB_BB_3BET = ActionClass("BTN vs SB/BB 3Bet", {"4-bet for Value": "AA AKs AQs AJs AKo KK AQo QQ JJ TT 99".split(),
                       "4-bet as a Bluff" : "K6s K5s K4s Q7s J7s QTo JTo K9o A8o 86s 75s 64s A5o 54s A4o 43s A3o".split(),
                       "Call" : "ATs A9s A8s A7s A6s A5s A4s A3s A2s KQs KJs KTs K9s K8s K7s KQo QJs QTs Q9s Q8s AJo KJo QJo JTs J9s J8s ATo KTo T9s T8s T7s A9o 98s 97s 88 87s 77 76s 66 65s 55 44 33 22".split()
                       })

# SB

SB_VS_BB_3BET = ActionClass("SB RFI vs BB 3Bet", {"4-bet for Value": "AA AKs AQs AJs AKo KK AQo QQ JJ".split(),
                       "4-bet as a Bluff" : "J4s Q5o Q4o K3o K2o".split(),
                       "Call" : "ATs KQs KJs KQo QJs AJo KJo ATo TT 99 95s 88 85s 74s 43s".split()
                       })

ALL_3BET_ACTIONS = [LJ_VS_HJ_3BET, LJ_VS_CO_3BET, LJ_VS_BTN_3BET, LJ_VS_SB_3BET, LJ_VS_BB_3BET
                    , HJ_VS_CO_3BET, HJ_VS_BTN_3BET, HJ_VS_SB_3BET, HJ_VS_BB_3BET,
                    CO_VS_BTN_SB_3BET, CO_VS_BB_3BET,
                    BTN_VS_SB_BB_3BET,
                    SB_VS_BB_3BET]


