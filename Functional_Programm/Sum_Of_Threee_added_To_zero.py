
"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
purpose:-sum of three number added to zero find
@author:-Sheevendra Singh Singraul
@version:-3.8.6
@since:-19-03-2021
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

def findTriplets(arr, n): #Giving findTriplets() defination
    found = False
    for i in range(0, n - 2):

        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):

                if (arr[i] + arr[j] + arr[k] == 0):
                    print("sum of these three number will be zero=",arr[i],"+",arr[j],"+",arr[k],"=0")
                    found = True

    if (found == False):        # If no triplet with 0 sum found in list[]
        print(" No sum of three number added to zero find")

arr=[]                          #declaring empty list
num=int(input("enter how many element you want to add into list="))
for i in range (num):           #runnung for loop to take input from user and appended into arr[] list
    element=int(input("enter list element="))
    arr.append(element)
print(arr)
n = len(arr)                    #using len() to get length of arr[] list
findTriplets(arr, n)            #action calling with parameter