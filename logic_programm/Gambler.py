import random
money=int(input("enter how much money gambler have="))
winningAmount=int(input("enter his winning amount="))
winPerTurn=int(input("how much he will win in each winning turn="))
winTurn=0
lossTurn=0
for i in range(money+1):
    element=random.randint(0,1)
    print("Dice rolled and you get=",element)
    if element==1:
        money+=winPerTurn
        winTurn+=1
        print("congrats you have won this turn and your winning money is=",money,"money")
        if money>=winningAmount:
            print("congrats you have win")
            break
    else:
        money-=1
        lossTurn+=1
        print("sorry you loss this time:now you have=",money)
        if money<=0:
            print("sorry you have loss all money")
print()
print("number of times gambler won=",winTurn)
print("number of times gambler loss=",lossTurn)
