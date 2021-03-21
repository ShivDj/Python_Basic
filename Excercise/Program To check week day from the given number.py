
"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* Purpose:  Program To check week day from the given number
* @author:  Sheevendra Singh Singraul
* @version: 3.8.6
* @since:   19-03-2021
*
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
num= int(input("enter day no please="))
if num > 7:
    print("you have entered number more then 7 please enter again but less then 7")
elif num==1:
    print("sunday")
elif num==2:
    print("monday")
elif num==3:
    print("tuesday")
elif num==4:
    print("wedensday")
elif num==5:
    print("thursday")
elif num==6:
    print("frieday")
elif num==7:
    print("satarday")
