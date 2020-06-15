from multiprocessing import Pool
import time

def f(n):
    sum = 0
    for x in range(100):
        sum+= n*n
    return sum

if __name__== "__main__":
    arr = [1,2,34]
    p = Pool()
    t1 = time.time()
    result = p.map(f, range(10000))
    print "Time take for pooled result: ", time.time()-t1

    result = []
    t2 = time.time()
    for x in range(10000):
        result.append(f(x))
    print "time taken by serial processing: " , time.time()-t2

