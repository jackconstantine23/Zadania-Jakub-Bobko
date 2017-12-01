#!/usr/bin/python

import threading
import time
import _thread

def jedzenie(nr, widelce, lock):
    
    print ("start")
    count = 0
    
    if ((nr+1)%5 > nr):
        widelce[nr%5].acquire()
        time.sleep(5)
        widelce[(nr+1)%5].acquire()
    else:
       widelce[(nr+1)%5].acquire()
       time.sleep(5)
       widelce[nr%5].acquire()

    print ("jem")

    if ((nr+1)%5 > nr):
        widelce[(nr+1)%5].release()
        widelce[nr%5].release()
    else:
       widelce[nr%5].release()
       widelce[(nr+1)%5].release()
       
    print ("end")

widelce = []
for i in range(0,5):
    widelce.append(threading.Lock())
lock = threading.Lock()

try:
   _thread.start_new_thread( jedzenie, (0, widelce, lock) )
   _thread.start_new_thread( jedzenie, (1, widelce, lock) )
   _thread.start_new_thread( jedzenie, (2, widelce, lock) )
   _thread.start_new_thread( jedzenie, (3, widelce, lock) )
   _thread.start_new_thread( jedzenie, (4, widelce, lock) )

except:
   print ("Error: unable to start thread")

print ("koniec")

