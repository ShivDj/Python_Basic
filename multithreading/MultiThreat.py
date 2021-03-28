
"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
purpose:-multithreading implementation
@author:-Sheevendra Singh Singhraul
@version:-3.8.6
@since:-28-03-2021
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
# Thread and time modules are imported
from threading import *
from time import  sleep
class hello(Thread):  #class created with name hello
    def run(self):    # method run is created
        for i in range (5): #for loop will run number of argument is passed to it
            print("Hello")
            sleep(1)   #sleep method ill hold the execution for 1 second

class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)


if __name__=="__main__":
    h=hello()
    hi=hi()

    h.start()
    sleep(0.3)
    hi.start()

    h.join()
    hi.join()
