"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
purpose:-Harmonic Number
@author:-Sheevendra Singh Singhraul
@version:-3.8.6
@since:-18-03-2021
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
userInput=int(input("enter anumber to find harmonic of it="))
harmonicNumber=1
if userInput > 0:
    for i in range (2,userInput+1):
        harmonicNumber+=1/i
    print("Harmonic number of number",userInput,"is=",harmonicNumber)
else:
    print("you have entered wrong input")