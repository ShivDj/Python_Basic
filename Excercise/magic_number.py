
"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* Purpose:  Program To find magic number
* @author:  Sheevendra Singh Singraul
* @version: 3.8.6
* @since:   19-03-2021
*
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
num=int(input("enter any number"))
temp=num
while temp>9:
    sum=0
    while temp!=0:
        rem=temp%10
        sum=sum+rem
        temp=int(temp/10)
    temp=sum
if sum==1:
    print(num,"is magic number")
else:
    print(num,"is not magic number")
    
    
  
