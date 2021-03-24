"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
purpose:-abstract base class work
@author:-Sheevendra Singh Singhraul
@version:-3.8.6
@since:-22-03-2021
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
class A:       #class A is created that is having one init and two function
    def __init__(self):
        print("cunstructor from class A")
    def add(self):
        print("from add method of class A")
    def sub(self):
        print("from sub method of class A")


class B():    # class B is created
    def __init__(self):
        print("cunstructure from class B")

    def add1(self):
        print("from add method of class B")

    def sub1(self):
        print("from sub method of class B")

class C(A,B):    #class is created and inherite class A and class B
    def __init__(self):
        super().__init__()    # using super method to specifically class init method of class A by rule of MRO
        print("cunstructure from class C")

    def add2(self):
        print("from add method of class C")

    def sub2(self):
        print("from sub method of class C")


c=C()  # c object is created of c class
