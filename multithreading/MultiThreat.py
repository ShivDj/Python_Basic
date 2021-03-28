
"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
purpose:-multithreading implementation
@author:-Sheevendra Singh Singhraul
@version:-3.8.6
@since:-28-03-2021
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
from threading import *
from time import  sleep
class hello(Thread):
    def run(self):
        for i in range (5):
            print("Hello")
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)

h=hello()
hi=hi()

h.start()
sleep(0.3)
hi.start()

h.join()
hi.join()
