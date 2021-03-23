"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* Purpose:  Program To Print Euclidean_Distance
* @author:  Sheevendra Singh Singraul
* @version: 3.8.6
* @since:   21-03-2021
*
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
import math as m            #math module imported
class Euclidean_Distance:   #class created
    def distance(self):     #class method created
        try:                #try block started
            x=int(input("enter value of x cordinate ="))
            y=int(input("enter value of y cordinate="))
            distanceCalculate = m.sqrt(x * x + y * y)
            print( "Calculate Distance between X and Y cordinate=",distanceCalculate)

        except ValueError:   #except block is started
            print("Integer expected but you have entered somthing else")
        except:
            print("something went wrong")

Euclidean=Euclidean_Distance() #object of class Euclidean created
Euclidean.distance()           #distance method is called by class object