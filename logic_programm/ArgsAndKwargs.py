"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
purpose:-programm to show args and kwargs
@author:-Sheevendra Singh Singhraul
@version:-3.8.6
@since:-22-03-2021
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
#function decliration
def sample(lst,*args,**kwargs):
    print("list",lst,args,kwargs)

#list creation
lst=[1,2,3,4,5,6,7,8,9,12,13]
#calling sample method by passing different parameter
sample(lst,"ankita","parhi","rishikesh","shamal",first="shiv",middel="singh",last="singhraul")