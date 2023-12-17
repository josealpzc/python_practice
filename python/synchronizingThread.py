#NOTE:This script contains examples from 'Thy Python Bible' book 
#This code will declare a variable x wich will be halved and doubled at the same time reaching a lock
#condition causing the code never to end. In order to fix it, we have declared a new Lock object (lock),
#by calling the function acquire, we will try to lock the resource if no body else is using it, and release it
#and release it with the release function, if lock has been 'locked' by someone else, the code will be
#executed until resoruces are released.
import threading
import time
import pdb

x = 8192
lock = threading.Lock()
def halve():
    global x,lock
    lock.acquire()
    #print(f"global {x}")
    #print('before')
    #breakpoint()
    #print('after')
    while(x>1):
        x/=2
        print(x)
        time.sleep(1)
    print('END!')
    lock.release()

def double():
    global x,lock
    lock.acquire()
    while(x < 16384):
        x*=2
        print(x)
        time.sleep(1)
    print('END!')
    lock.release()

t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)

t1.start()
t2.start()
