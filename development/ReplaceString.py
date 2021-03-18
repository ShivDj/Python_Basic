
"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
purpose:-User Input and Replace String Template “Hello <<UserName>>, How are you?”
@author:-Sheevendra Singh Singhraul
@version:-3.8.6
@since:-18-03-2021
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

stringInputByUser=input("Enter Your good name please=")
if len(stringInputByUser) >= 3:
    print("HELLO" ,stringInputByUser, "HOW ARE YOU")
else:
    print("You have entered String which is less them [3] char Please enter String More then 3 char= ")
