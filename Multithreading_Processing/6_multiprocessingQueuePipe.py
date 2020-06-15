import multiprocessing


def calSquare(numbers,q):
    for n in numbers:
        q.put(n*n)


if __name__=="__main__":
    numbers = [2,5,8]
    q= multiprocessing.Queue()
    p = multiprocessing.Process(target=calSquare, args=(numbers,q))
    p.start()
    p.join()
    while q.empty() is False:
        print q.get()

