
"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* Purpose:  Program To find second max variable in a given list
* @author:  Sheevendra Singh Singraul
* @version: 3.8.6
* @since:   19-03-2021
*
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
list=[23,21,43,45,0,8,6,54,53]
if list[0] > list[1]:
    mx = list[0]
else:
    mx = list[1]
    secondmx = list[0]
n=len(list)
for i in range (2,n):
    if list[i]>mx:
        secondmx=mx
        mx=list[i]
    elif list[i] > secondmx and mx != list[i] :
        secondmx = list[i]
print (secondmx)
