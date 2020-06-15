import multiprocessing


def calSquare(numbers,v,result):
    v.value = 5.6666
    for idx,n in enumerate(numbers):
        result[idx] = n*n
    print "inside the process: ", result[idx]


if __name__=="__main__":
    numbers = [2,5,8]
    result = multiprocessing.Array('i',3)                   #'i' : type and 3: number of process
    v= multiprocessing.Value('d', 0.0)
    p = multiprocessing.Process(target=calSquare,
                                args=(numbers,v,result))
    p.start()
    p.join()
    print "Getting value outside the process: ", v.value


