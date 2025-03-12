from actionClass import ActionClass

# HJ

HJ_VS_LJ_RFI = ActionClass("HJ vs LJ Raise First In", 
                      {"3-bet": "AA AKs AQs AJs ATs A5s AKo KK KQs KJs KTs AQo KQo QQ QJs JJ TT 99".split()})

# CO

CO_VS_LJ_RFI = ActionClass("CO vs LJ Raise First In", 
                      {"3-bet": "AA AKs AQs AJs ATs A5s AKo KK KQs KJs KTs AQo KQo QQ QJs JJ TT 99 88".split()})

CO_VS_HJ_RFI = ActionClass("CO vs HJ Raise First In", 
                      {"3-bet": "AA AKs AQs AJs ATs A9s A5s A4s AKo KK KQs KJs KTs AQo KQo QQ QJs AJo JJ TT 99 88".split()})

# BTN

BTN_VS_LJ_RFI = ActionClass("BTN vs LJ Raise First In", 
                      {"3-bet": "AA AKs AQs A9s A8s A4s A3s AKo KK K9s KQo QQ QJs AJo JJ T9s".split(),
                       "Call" : "AJs ATs A5s KQs KJs KTs AQo QTs JTs TT 99 88 77 76s 66 65s 55 54s".split()})

BTN_VS_HJ_RFI = ActionClass("BTN vs HJ Raise First In", 
                      {"3-bet": "AA AKs AQs A9s A8s A7s A4s A3s AKo KK KTs K9s K8s KQo QQ QTs Q9s AJo JJ T9s 66".split(),
                       "Call" : "AJs ATs A5s KQs KJs AQo QJs JTs TT 99 98s 88 87s 77 55 44".split()})

BTN_VS_CO_RFI = ActionClass("BTN vs CO Raise First In", 
                      {"3-bet": "AA AKs AQs A8s A7s A6s A4s A3s AKo KK KQs K9s KQo QQ QJs Q9s AJo KJo QJo JJ JTs J9s ATo TT 55".split(),
                       "Call" : "AJs ATs A9s A5s KJs KTs AQo QTs T9s 99 98s 88 77 66".split()})

# SB

SB_VS_LJ_RFI = ActionClass("SB vs LJ Raise First In", 
                      {"3-bet": "AA AKs AQs AJs ATs A5s AKo KK KQs KJs KTs AQo QQ QJs JJ TT 99".split(),
                     })

SB_VS_HJ_RFI = ActionClass("SB vs HJ Raise First In", 
                      {"3-bet": "AA AKs AQs AJs ATs A5s AKo KK KQs KJs KTs AQo QQ QJs QTs JJ JTs TT 99 88 77".split(),
                       })

SB_VS_CO_RFI = ActionClass("SB vs CO Raise First In", 
                      {"3-bet": "AA AKs AQs AJs ATs A9s A5s AKo KK KQs KJs KTs AQo KQo QQ QJs QTs AQo KQo QQ QJs QTs JJ JTs J9s TT T9s 99 88 77 66".split()})


SB_VS_BTN_RFI = ActionClass("SB vs BTN Raise First In", 
                      {"3-bet": "AA AKs AQs AJs ATs A9s A8s A7s A5s A4s AKo KK KQs KJs KTs K9s AQo KQo QQ QJs QTs Q9s AJo KJ0 JJ JTs J9s TT T9s T8s 99 88 77 66 55".split()})
SB_LIMP_VS_BB_RAISE = ActionClass("SB vs BTN Raise First In", 
                      {"4-bet for Value": "AA AKs AQs AJs ATs AKo KK KQs KJs AQo KQo QQ QJs AJo KJo JJ ATo TT 99 88".split(),
                       "3-bet as a Bluff" : "Q7o K6o K5o A3o A2o".split(),
                       "Call": "A9s A8s A7s A6s A5s A4s A3s A2s KTs K9s K8s K7s K6s K5s K4s K3s K2s QTs Q9s Q9s Q8s Q7s Q6s Q5s Q4s Q3s Q2s QJo JTs J9s J8s J7s J6s J5s J4s J3s J2s KTo QTo JTo J9s J8s J7s J6s J5s KTo Qto JTo T9s T8s T7s T6s KTo QTo JTo T9s T8s T7s T6s KTo QTo JTo T9s T8s T7s T6s A9o K9o Q9o J9o T9o 98s 97s 96s A8o K8o Q8o J8o T8o 98o 87s 86s A7o K7o 97o 87o 77 76s 75s A6o 76o 66 65s 64s A5o 55 54s A4o 44 33 32s 22".split()})
# BB

BB_VS_LJ_RFI = ActionClass("BB vs LJ Raise First In", 
                      {"3-bet": "AA AKs AQs A5s A4s AKo KK KQs KJs QQ QJs JJ JTs 65s 54s".split(),
                       "Call" : "AJs ATs A9s A8s A7s A6s A3s A2s KTs K9s K8s K7s K6s K5s K4s K3s K2s AQo KQo QTs Q9s Q8s Q7s Q6s Q5s AJo KJo QJo J9s J8s ATo JTo TT T9s T8s T7s 99 98s 97s 96s 88 87s 86s 85s 77 76s 75s 74s 66 64s 63s 55 53s 44 43s 33 32s 22".split()
                     })

BB_VS_HJ_RFI = ActionClass("BB vs HJ Raise First In", 
                      {"3-bet": "AA AKs AQs A9s A5s A4s AKo KK KQs KJs KTs K5s QQ QJs QTs JJ JTs TT 65s 54s".split(),
                       "Call" : "AJs ATs A8s A7s A6s A3s A2s K9s K8s K7s K6s K4s K3s K2s AQo KQo Q9s Q8s Q7s Q6s Q5s AJo KJo QJo J9s J8s J7s ATo KTo QTo JTo T9s T8s T7s A9o 99 98s 97s 96s 88 87s 86s 85s 77 76s 75s 74s 66 64s 63s 55 53s 44 43s 33 22".split()
                     })

BB_VS_CO_RFI = ActionClass("BB vs CO Raise First In", 
                      {"3-bet": "AA AKs AQs AJs A9s A5s A4s AKo KK KQs KJs KTs AQo QQ QJs QTs Q9s JJ JTs J9s TT T9s 99 65s 54s".split(),
                       "Call" : "ATs A8s A7s A6s A3s A2s K9s K8s K7s K6s K5s K4s K3s K2s KQo Q8s Q7s Q6s Q5s Q4s Q3s AJo KJo QJo J8s J7s J6s ATo KTo QTo JTo T8s T7s A9o T9o 98s 97s 96s A8o 88 87s 86s 85s 77 76s 75s 74s 66 64s 63s A5o 55 53s 52s 44 43s 33 22".split()
                     })

BB_VS_BTN_RFI = ActionClass("BB vs BTN Raise First In", 
                      {"3-bet": "AA AKs AQs AJs ATs A6s A5s A4s AKo KK KQs KJs KTs K9s AQo KQo QQ QJs QTs Q9s JJ JTs J9s J8s TT T9s T8s 99 98s 97s 88 87s 76s 65s 54s".split(),
                       "Call" : "A9s A8s A7s A3s A2s K8s K7s K6s K5s K4s K3s K2s Q8s Q7s Q6s Q5s Q4s Q3s Q2s AJo KJo QJo J7s J6s J5s J4s J3s J2s ATo KTo QTo JTo T7s T6s T5s T4s T3s T2s A9o K9o Q9o J9o T9o 96s 95s 94s A8o K8o Q8o J8o T8o 98o 86s 85s 84s A7o K7o 87o 77 75s 74s 73s A6o K6o 76o 66 64s 63s 62s A5o 65o 55 53s 52s A4o 54o 44 43s 42s 33 32s 22".split()
                     })

BB_VS_SB_LIMP = ActionClass("BB vs SB Limp", 
                      {"3-bet": "AA AKs AQs AJs ATs A9s A8s A5s A4s A3s AKo KK KQs KJs KTs K9s K6s K5s AQo KQo QQ QJs QTs Q9s AJo KJo JJ JTs J9s J8s J2s ATo JTo TT T9s T8s T4s T3s T3s T2s T9o 99 98s 97s 94s 93s 92s 88 87s 86s 84s J7o 77 76s 75s 74s 73s Q6o J6o T6o 96o 66 65s 64s 63s A5o K5o Q5o J5o T5o 95o 85o 75o 55 54s K4o Q4o 74o 44 33 32s".split(),
                       "Call" : "A7s A6s A2s K8s K7s K4s K3s K2s Q8s Q7s Q6s Q5s Q4s Q3s Q2s QJo J7s J6s J5s J4s J3s KTo QTo T7s T6s T5s A9o K9o Q9o J9o 96s 95s A8o K8o Q8o J8o T8o 98o 85s 83s 82s A7o K7o Q7o T7o 97o 87o 72s A6o K6o 86o 76o 62s 65o 53s 52s A4o J4o T4o 94o 84o 64o 54o 43s 42s A3o K3o Q3o J3o T3o 93o 83o 73o 63o 53o 43o A2o K2o Q2o J2o T2o 92o 82o 72o 62o 52o 42o 32o 22".split()
                     })

BB_VS_SB_RAISE = ActionClass("BB vs SB Raise", 
                      {"3-bet": "AA AKs AQs AJs ATs A5s A4s AKo KK KQs KJs KTs AQo QQ QJs JJ J5s TT T5s 99 95s J8o 88 87s J7o T7o 76s A6o K6o Q6o 65s K5o 54s".split(),
                       "Call" : "A9s A8s A7s A6s A3s A2s K9s K8s K7s K6s K5s K4s K3s K2s KQo QTs Q9s Q8s Q7s Q6s Q5s Q4s Q3s Q2s AJo KJo QJo JTs J9s J8s J7s J6s J4s J3s J2s ATo KTo QTo JTo T9s T8s T7s T6s T4s T3s T2s A9o K9o Q9o J9o T9o 98s 97s 96s 96s 94s 93s 92s A8o K8o Q8o T8o 98o 86s 85s 84s A7o K7o Q7o 97o 87o 77 75s 74s 73s 86o 76o 66 64s 63s 62s A5o 65o 55 53s 52s A4o 54o 44 43s 42s A3o 33 32s A2o".split()
                     })




ALL_FACING_RFI_ACTIONS = [HJ_VS_LJ_RFI,
                          CO_VS_LJ_RFI, CO_VS_HJ_RFI,
                          BTN_VS_LJ_RFI, BTN_VS_HJ_RFI, BTN_VS_CO_RFI,
                          SB_VS_LJ_RFI, SB_VS_HJ_RFI, SB_VS_CO_RFI, SB_VS_BTN_RFI, SB_LIMP_VS_BB_RAISE,
                          BB_VS_SB_LIMP, BB_VS_BTN_RFI, BB_VS_CO_RFI, BB_VS_HJ_RFI, BB_VS_LJ_RFI, BB_VS_SB_RAISE]