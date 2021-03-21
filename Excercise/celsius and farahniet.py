
"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* Purpose:  Program To calculate farenheit and celsius
* @author:  Sheevendra Singh Singraul
* @version: 3.8.6
* @since:   19-03-2021
*
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
cel = int(input("enter value in celsius="))
farenheit = int(input("enter value in farenheit="))
def conv(i):
    switcher = {
        0: cel(),
        1: fer(),
    }
    return switcher.get(i, "Invalid input")
def fer():
    farenheit = ((Cel * 9)/5)+32
    print(("celsius=",celsius, "farenheit=",fahrenheit))
def cel():
    calcel = (farenheit–32)*5/9
    print(( "farenheit=", fahrenheit,"celsius=", celsius))
