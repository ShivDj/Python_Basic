"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* Purpose:  Program To check second lagest and smallest number in list
* @author:  Sheevendra Singh Singraul
* @version: 3.8.6
* @since:   19-03-2021
*
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
list1 = []
import random
for i in range (1,11):
    element=random.randint(99,999)
    list1.append(element)
print("original array",list1)
#[12,43,0,89,56,21]
largest = list1[0]
lowest = list1[0]
largest2 = None
lowest2 = None
for item in list1[1:]:
    if item > largest:
        largest2 = largest
        largest = item
    elif largest2 == None or largest2 < item:
        largest2 = item
    if item < lowest:
        lowest2 = lowest
        lowest = item
    elif lowest2 == None or lowest2 > item:
        lowest2 = item

print("Second Largest element is:", largest2)
print("Second Smallest element is:", lowest2)

