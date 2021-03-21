"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* Purpose:  Program to check given date is present in given range of month from march20 to june20
* @author:  Sheevendra Singh Singraul
* @version: 3.8.6
* @since:   19-03-2021
*
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

date= int(input("Enter Date:-"))
Month= int(input("Enter month:-"))
if (Month <= 6 & date <= 20):
    print(Month ,date ,"True")

elif ((Month >= 3 & Month < 6) & (date<31)  ):
    print(date,Month ,"True")
else:
    print("False")
