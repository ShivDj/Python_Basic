"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* Purpose:  programm to check given year is leap or not 
* @author:  Sheevendra Singh Singraul
* @version: 3.8.6
* @since:   19-03-2021
*
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
year= int(input("Enter year:-"))
result= "leap year" if year%400==0 else "leap year" if year%4==0 and year%100 else "none leap year"
print (result)
