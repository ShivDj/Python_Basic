"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
purpose:-programm for stop watch
@author:-Sheevendra Singh Singhraul
@version:-3.8.6
@since:-22-03-2021
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
import time  # importing time module
while True:  #while loop will run untill condition false
    try:     # try block is used to handle excepon
        input("please ENTER to start , CTRL_C to exit")
        start_time=time.time()     # time.time() method give us current time
        print("timer has started")
        while True:
            print("Timer elapsed=",round(time.time()-start_time,0),"sec",end="\n")
            time.sleep(1)  #sleep method will pause execution for 1 second every iteration
    except KeyboardInterrupt:
        print("Timer has stopped")
        end_time=time.time()
        print("The time elapsed is",round(end_time-start_time),"sec")
        break
