from multiprocessing import Process, BoundedSemaphore
from multiprocessing import current_process
from multiprocessing import Value, Array
import random
import time

N = 8

def task(semaphore, common, tid):
    a = 0
    for i in range(6):

        print(f'{tid}-{i}: Non-critical Section', flush=True)
        a += 1
        time.sleep(random.random())
        print(f'{tid}-{i}: End of non-critical Section', flush=True)
        semaphore.acquire()

        print(f'{tid}-{i}: Critical section', flush=True)
        v = common.value + 1
        print(f'{tid}-{i}: Inside critical section', flush=True)
        time.sleep(random.random())
        common.value = v
        print(f'{tid}-{i}: End of critical section', flush=True)

        semaphore.release()

def main():
    K = 5
    semaphore = BoundedSemaphore(K)
    lp = []
    common = Value('i', 0)
    for tid in range(N):
        lp.append(Process(target=task, args=(semaphore, common, tid)))
    print (f"Valor inicial del contador {common.value}", flush=True)
   
    for p in lp:
        p.start()
    for p in lp:
        p.join()
    print (f"Valor final del contador {common.value}", flush=True)
    print ("fin")

if __name__ == "__main__":
    main()
