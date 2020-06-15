class RemoteControl:
    def __init__(self):
        self.channel = ["BBC", "Aljajeera", "CNN", "ESPN"]
        self.index = -1
        print dir(self)

    def __iter__(self):
        return self

    # def __next__(self):
    #     self.index+=1
    #     if self.index == len(self.channel):
    #         raise StopIteration
    #     return self.channel[self.index]

if __name__=="__main__":
    r= RemoteControl()
    itr = iter(r)
    print itr.next()
    # print next(itr)
    # print next(itr)
    # print next(itr)
    # print next(itr)
    # print next(itr)
