
"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* Purpose:  finding the minimum and maximum value from given arthimatic operation
* @author:  Sheevendra Singh Singraul
* @version: 3.8.6
* @since:   19-03-2021
*
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
a= int(input("enter value of A please="))
b= int(input("enter value of B please="))
c= int(input("enter value of C please="))
first=a+b*c
second=c+a/b
third=a%b+c
fourth=a*b+c
print ("a+b*c=",first)
print("c+a/b=",second)
print("a%b+c=",third)
print("a*b+c=",fourth)
print(first if first > second and first >third and first > fourth else second if second > third and second > fourth else third if third > fourth else fourth)
print(first if first < second and first <third and first < fourth else second if second < third and second < fourth else third if third < fourth else fourth)
