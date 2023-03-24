from queue import Queue
from threading import Thread
import time


class CustomThread(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return

def f1(x):
    print(f"in f1 : {x}")
    time.sleep(7)
    return True

def f2(y):
    print(f"in f2 : {y}")
    time.sleep(2)
    return "hello"

def f3(z, g):
    print(f"in f3 : {z} {g}")
    time.sleep(5)
    return True

def f4(z):
    print(f"in f4 : {z} ")
    time.sleep(5)
    return "now that's a 4"

def f5(z):
    print(f"in f5 : {z}")
    time.sleep(5)
    return True

def f6(z):
    print(f"in f6 : {z}")
    time.sleep(5)
    return True

def do_stuff(q):
  while True:
      item = q.get()
      if item:
          print(item)
          item.start()
          response = item.join()
          print(response)
          q.task_done()

q = Queue(maxsize=0)
num_threads = 4

for i in range(num_threads):
  worker = Thread(target=do_stuff, args=(q,))
  worker.setDaemon(True)
  worker.start()

start = time.time()


q.put(CustomThread(target=f1, args=(1,)))
q.put(CustomThread(target=f2, args=(2,)))
q.put(CustomThread(target=f3, args=(3,5)))
q.put(CustomThread(target=f4, args=(4,)))
q.put(CustomThread(target=f5, args=(5,)))
q.put(CustomThread(target=f6, args=(6,)))
q.join()
print(f"Total time taken : {time.time() - start}")
