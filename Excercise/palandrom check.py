
"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* Purpose:  Program to check first number is palandrom to other or not
* @author:  Sheevendra Singh Singraul
* @version: 3.8.6
* @since:   19-03-2021
*
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
temp=n1
rev=0
while(n1>0):
    dig=n1%10
    rev=rev*10+dig
    n1=n1//10
if(n2==rev):
    print("The n1 is palindrome! for n2")
else:
    print("The n1 isn't palindrome! for n2"
