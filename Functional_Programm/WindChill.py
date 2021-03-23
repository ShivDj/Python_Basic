"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
purpose:-calculate WindChill
@author:-Sheevendra Singh Singhraul
@version:-3.8.6
@since:-18-03-2021
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
from math import pow
t=0
try:
    t1=float(input("enter tempreture in farahniet="))
    if t1>50:
        print("you have entered wrong farahniet ")
    else:
       t=t1

    v1=float(input("enter the wind speed in MPH="))
    if v1>120 and v1<3:
        print("you have entered wrong wind speed")
    else:
        v=v1
        print("power of v and t=",pow(t,v))

    #w=35.74+0.2625t+(42.75t-35.75)v0.16
except NameError:
            print("something went wrong")

