import time
import multiprocessing

def deposit(balance, lock):
    print "started in deposit"
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        print "Locked in deposit"
        balance.Value = balance.value+1
        lock.release()

def withdraw(balance, lock):
    print "start in withdraw"
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        print "locked in withdraw"
        balance.Value = balance.value - 1
        lock.release()

if __name__ == "__main__":
    balance = multiprocessing.Value('i',200)
    lock = multiprocessing.Lock()
    d= multiprocessing.Process(target=deposit, args=(balance,lock))
    w = multiprocessing.Process(target=withdraw, args=(balance,lock))
    d.start()
    w.start()
    d.join()
    w.join()
    print balance.value