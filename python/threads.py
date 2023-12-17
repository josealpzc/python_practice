#Author: Jose Antonio Lopez
#Note: This script contains some examples from 'The Python Bible' book
import threading

def hello():
    print("Hello World!")


#t1 = threading.Thread(target=hello)
#t1.start()

def function1():
    for i in range(1000):
        print('ONE')

def function2():
    for i in range(1000):
        print('TWO')
'''
#call the class Thread within the imported module 'threading'
t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)

#This threads run in parallel
#Alternates between ONE and TWO
#t1.start()
#t2.start()

#This thread run serially
#You will first see ONE and then TWO.
t1.run()
t2.run()
'''
#WAITING FOR THREADS
def function():
    for i in range(500000):
        print('hello world')

#Create a new object of Thread type.
t1 = threading.Thread(target=function)

#Start the tread (parallel)

#t1.start()

#Here we wait for the thread to finish 
#t1.join()

#print("THIS IS THE END!")

'''
                THREAD CLASS
'''
class  MyThread(threading.Thread):
    def __init__(self,message):
        threading.Thread.__init__(self)
        self.message=message

    def run(self):
        for x in range(100):
            print(self.message)

mt1=MyThread("This is my thread message!")
mt1.start()
