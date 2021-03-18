"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
purpose:-Programm to check entered year is leap year or not
@author:-Sheevendra Singh Singhraul
@version:-3.8.6
@since:-18-03-2021
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
inputyear = int(input("Enter a year: "))
if inputyear > 0:
    if (inputyear % 4) == 0:
       if (inputyear % 100) == 0:
           if (inputyear % 400) == 0:
               print(inputyear," is a leap year")
           else:
               print(inputyear," is a leap year")
       else:
           print(inputyear," is a leap year")
    else:
       print(inputyear, "is not a leap year")
else:
    print("you have entered NAGATIVE value",inputyear,"Please enter positive value to check leap year")