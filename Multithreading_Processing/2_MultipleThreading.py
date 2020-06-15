import logging
import time
import threading

def multipleThreading(num):
    print "Starting the thread : ",num
    time.sleep(2)
    print"Ending the thread : ", num

if __name__ == "__main__":
    print "main....."
    print "heiloo"
    threads = list()
    for index in range(3):
        print "creating and start thread : ", index
        th = threading.Thread(target=multipleThreading, args=(index,))
        threads.append(th)
        th.start()
    for index, thread in enumerate(threads):
        print"Main    : before joining thread ", index
        thread.join()
        print"Main    : thread {} done".format(index)
