import numpy as np
import pandas as pd
import json

D = pd.read_json("Deck.json")    #The deck
O = np.arange(52)                #The order
np.random.shuffle(O)             #The Shuffle

#Hand of The House and the player
MHand = 0
Hand = 0

lost = 0                         #Indicator you lost
#indicator of Hit or stay is Flag

#The House's Hand
Flag = 1
MHand += np.random.randint(12)
MHand1 = MHand                   #The House's visible card
MHandc = 0                       #The House's number of hidden cards
while Flag==1:
    LC = np.random.randint(12)   #Last Card added (cause The House cheats)
    MHand += LC
    MHandc += 1
    if MHand >=21:
        MHand -= LC
        MHandc -= 1
        Flag = 0
        print(f"The House has: {MHand1} with {MHandc} hidden cards")


#Your Hand
Flag = 1
while Flag==1:
    if Hand <= 21:
        print(f"you have: {Hand}")
        Flag = input("type 1 to hit and 0 to stay:")
        Flag = int(Flag)
    else:
        print("You Burned")
        lost = 1
        break
    if Flag ==1:
        Hand += np.random.randint(12)

if Hand > MHand and lost == 0:
    print(f"you won, you had {Hand}, The House had {MHand}")
else:
    print(f"you lost, you had {Hand}, The House had {MHand}")