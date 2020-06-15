import multiprocessing

result = list()
def calSquare(numbers):
    global result
    for n in numbers:
        result.append(n*n)
    print "inside the process: ", result


if __name__=="__main__":
    numbers = [2,5,8]
    p = multiprocessing.Process(target=calSquare, args=(numbers,))
    p.start()
    p.join()
    print "outside the process: ", result

