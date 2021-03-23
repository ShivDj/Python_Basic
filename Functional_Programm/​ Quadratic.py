"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* Purpose:  Program To calculate the roots of the equation
* @author:  Sheevendra Singh Singraul
* @version: 3.8.6
* @since:   21-03-2021
*
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
import math      #math module imported
class Quadratic:
    def cal(self):
        try:             #try block is used to limiting value of b more then a and c
            a=int(input("enter the value of a="))
            b=int(input("enter the value of B="))
            c=int(input("enter the value of C="))

            delta = b*b - 4*a*c
            root1_Of_x = (-b + (math.sqrt(delta))/(2*a))
            root2_Of_x = (-b - (math.sqrt(delta))/(2*a))
            print("first Quadratic root_1=",root1_Of_x)
            print("second Quadratic root_2=",root2_Of_x)
        except ValueError: #if b value is given less then a and c then ValueError occure that handled in here
            print("you have to give b value more then a and c")

        except:         #all other exceptions are handled here
            print("something wenrt wrong")


q=Quadratic()
q.cal()