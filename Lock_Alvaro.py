from multiprocessing import Process, Lock, Value
import time
import random

    
def task(common,tid,semaphore):
    for i in range(5):
        print(f'{tid}-{i}: Non-critical Section', flush=True)
        time.sleep(random.random())
        print(f'{tid}-{i}: End of non-critical Section', flush=True)
        semaphore.acquire()
        print (f"{tid}-{i}: start of critical section")
        v = common.value + 1
        print (f"{tid}-{i}: inside of critical section")
        time.sleep(random.random())
        common.value = v  
        print (f"{tid}-{i}: end of critical section")
        semaphore.release()


def main():
    lp = []
    common = Value('i', 0)
    semaphore = Lock()
    for tid in range(5):
        lp.append(Process(target=task, args=(common,tid,semaphore)))
    print (f"Valor inicial del contador {common.value}",flush = True)
    for p in lp:
        p.start()

    for p in lp:
        p.join()

    print (f"Valor final del contador {common.value}",flush = True)
    print ("fin")          

if __name__ == "__main__":
    main()