"""
Author: Jose Lopez
Notes: This is an example from 'The Python Bible'
This script will declare a semaphore by calling the BoundedSemaphore class within threading module. Access allowed
to semaphore will be determined by the 'value' parameter, same as in thread, access to threads is initialized 
by the acquire function, this will allow us to use 5 threads in parallel and continue to execute the code 
once some other thread is free.1
"""

import threading
import time

semaphore = threading.BoundedSemaphore(value=5)

def access(thread_number):
    print("{}: Trying access...".format(thread_number))
    semaphore.acquire()
    print("{}: Access granted!".format(thread_number))
    print("{}: Waiting 5 seconds...".format(thread_number))
    time.sleep(5)
    semaphore.release()
    print("{}: Releasing!".format(thread_number))

for thread_number in range(10):
    t = threading.Thread(target=access,args=(thread_number,))
    t.start()

