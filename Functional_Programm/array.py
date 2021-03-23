
"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
purpose:-2D array
@author:-Sheevendra Singh Singhraul
@version:-3.8.6
@since:-18-03-2021
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
import array

rows=int(input("enter how many rows you want in array="))
columns=int(input("enter how many columns you want in array="))

print( [[0 for x in range(rows)] for x in range(columns)])

class TwoDimenson:

 def display(array):
        for r in array:
            for c in r:
                print([c],end = " ")
            print()
        print()

Two=TwoDimenson()
Two.display(IntegerArray)
Two.display(FloatArray)
Two.display(StringArray)