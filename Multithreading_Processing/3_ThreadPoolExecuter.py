import concurrent.futures
import time

def multipleThreading(num):
    print "Starting the thread : ",num
    time.sleep(2)
    print"Ending the thread : ", num

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(multipleThreading, range(3))