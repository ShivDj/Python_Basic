"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* Purpose:  Program To Print sum of 5 random 2 digit no
* @author:  Sheevendra Singh Singraul
* @version: 3.8.6
* @since:   19-03-2021
*
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
import random
i=0
sum=0
count=5
while i<count:
    add=(random.randrange(10,99,) )
    print(add)
    sum=sum+add
    i=i+1
print("sum of 5 random 2 digit no is=>",sum)
print("averag of 5 random 2 digit no is=>",sum/count)
