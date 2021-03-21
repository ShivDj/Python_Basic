
"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* Purpose:  Program To Print head and tail percentages
* @author:  Sheevendra Singh Singraul
* @version: 3.8.6
* @since:   19-03-2021
*
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
import random
head=0
tail=0
for i in range (1,22):
    flip= random.randint(0,1)
    if flip==1:
        head+=1
        print("head",end=",")
        if head==11:
            break
    else:
        tail+=1
        print("tail",end=",")
        if tail==11:
            break
print()
print("head",head)
print("tail",tail)
