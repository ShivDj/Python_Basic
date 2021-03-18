"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
purpose:-Computes the prime factorization of N
@author:-Sheevendra Singh Singhraul
@version:-3.8.6
@since:-18-03-2021
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
userInput=int(input("enter a number to check for prime factorial="))
prime_number=[]
devisor=2
while devisor<=userInput:
    if userInput%devisor==0:
        prime_number.append(devisor)
        userInput=userInput/devisor
    else:
        devisor+=1

print(prime_number)