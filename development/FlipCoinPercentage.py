"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
purpose:-Flip Coin and print percentage of Heads and Tails
@author:-Sheevendra Singh Singhraul
@version:-3.8.6
@since:-18-03-2021
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

import random
head=0
tail=0
inputByUser=int(input("Enter number of times you wanna to FLIP the COIN="))
if inputByUser>=0:
    for i in range (inputByUser):
       randomValue=random.randint(0,1)
       if randomValue>0.5:
           head +=1
       else:
           tail +=1

    print("COIN flip by user=", inputByUser, "times")
    print("HEAD is comming=",head,"times")
    print("TAIL is comming= ",tail)
    print()
    print("Percentage of HEAD=",(head/inputByUser)*100,"And Percentage of TAIL",(tail/inputByUser)*100)

else:
    print("you have entered nagative integer value\n please enter positive value")

