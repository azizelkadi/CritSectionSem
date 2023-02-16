
from multiprocessing import Process, current_process,BoundedSemaphore, Value
import time
import random

def non_critical(tid,i):
    print(f'{tid}-{i}: Non-critical Section', flush=True)
    time.sleep(random.random())
    print(f'{tid}-{i}: End of non-critical Section', flush=True)
    
def critical(common,tid,i):
    print (f"{tid}-{i}: start of critical section")
    v = common.value + 1
    print (f"{tid}-{i}: inside of critical section")
    time.sleep(random.random())
    common.value = v  
    print (f"{tid}-{i}: end of critical section")
    
def task(common,tid,semaphore):
    for i in range(5):
        non_critical(tid,i)
        semaphore.acquire()
        critical(common,tid,i)
        semaphore.release()


def main():
    lp = []
    common = Value('i', 0)
    semaphore = BoundedSemaphore(1)
    for tid in range(5):
        lp.append(Process(target=task, args=(common,tid,semaphore)))
    print (f"Valor inicial del contador {common.value}")
    for p in lp:
        p.start()

    for p in lp:
        p.join()

    print (f"Valor final del contador {common.value}")
    print ("fin")          

if __name__ == "__main__":
    main()