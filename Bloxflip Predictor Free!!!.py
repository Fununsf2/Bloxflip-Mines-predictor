import random
from time import sleep
print("I would like to note that this is going to be used on 5 bombs as that is the best! Enjoy!")
sleep(2)
while True:
    try:
        MinesAmount = random.randint(2,4)
        if MinesAmount == 2:
            print("2 Mines what to do:")
            RandomValue = print(random.randint(1,12))
            Randomvalue2 = print(random.randint(13,25))
        if MinesAmount == 3:
            print("3 Mines what to do:")
            Randomvalue = print(random.randint(1,8))
            Rnaomdvalue2 = print(random.randint(9,17))
            RandomValue3 = print(random.randint(18,25))
        if MinesAmount == 4:
            print("4 Mines what to do:")
            Randomvalue = print(random.randint(1,6))
            Rnaomdvalue2 = print(random.randint(7,12))
            RandomValue3 = print(random.randint(13,18))
            RandomValue3 = print(random.randint(19,25))
        ToNextRound = input(" ")
    except:
        print("IDK not my problem lmao")