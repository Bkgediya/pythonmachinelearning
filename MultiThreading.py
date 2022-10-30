
#MultiThreading


import time
import threading

def list_append(count,sign = 1 ,out_list = None):
     if out_list is None:
         out_list  = list()
     for i in range(count):
         out_list.append(sign*i)
         sum(out_list) # do sum computation
     return out_list

size = 10000
out_list = list()

thread1 = threading.Thread(target = list_append,args = (size,1,out_list))
thread2 = threading.Thread(target = list_append,args = (size,-1,out_list))

starttime = time.time()

# execute both in parallel

thread1.start()
thread2.start()

#back to parent process
thread1.join()
thread2.join()

#print("Threading ellapsed time ",time.time - starttime)

print(out_list[:100])    
