"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
purpose:-Power of 2
@author:-Sheevendra Singh Singhraul
@version:-3.8.6
@since:-18-03-2021
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
import math
useInput=int(input("Enter a Integer number to check for its power of 2="))  #5
if useInput > 0 and useInput<31:
    for i in range(1, useInput+1):
        print("power of 2**",i,"=",2**i)

else:
    print(" please enter value between 1 to 30 THNKYOU")