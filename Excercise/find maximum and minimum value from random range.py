
"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* Purpose: find maximum and minimum value from random range  
* @author:  Sheevendra Singh Singraul
* @version: 3.8.6
* @since:   19-03-2021
*
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
import random
list=[]
for i in range(1,6):
    element=random.randrange(99,1000)
    list.append(element)
print(list)
print("getting maximum element by using max function=",max(list))
print("getting minimum element by using min function=",min(list))
mx=(list[0])
for j in list:
    if j> mx:
        mx=j
print("maximum element using if else logic=",mx)
min=(list[0])
for j in list:
    if j<min:
        min=j
print("minimum element using if else logic=",min)
