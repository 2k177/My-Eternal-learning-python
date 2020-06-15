import threading
import time

def calSquare(number):
    print "calculating squres.....\n"
    time.sleep(2)

    for n in number:
        time.sleep(0.2)
        print  "square", n*n
    print "done in 1"

def calCube(number):
    print "calculating cubes.....\n"
    time.sleep(2)
    for n in number:
        time.sleep(0.2)
        print "cube", n*n*n
    print "done in 2"

num = [2,6,7,9]
t= time.time()
th1 = threading.Thread(target=calSquare, args=(num,))
th2 = threading.Thread(target=calCube, args=(num,))

th1.start()
th2.start()

th1.join()
th2.join()

print "\ncompleted in time: ", time.time()-t                #takes approx 2 sec
print "\ncompleted threads"

#Testing without the threads
print "time taken without threading for the same"           #takes approx: 4sec
t= time.time()
calSquare(num)
calCube(num)
print "\ncompleted in time: ", time.time()-t

