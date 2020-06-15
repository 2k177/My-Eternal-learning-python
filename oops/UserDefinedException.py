class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
        self.x =1/0
    def handle(self):
        print "Accident here @ point X, pass information"

try:
    raise Accident("Crash between two cars")
except Accident as e:
    e.handle()
finally:
    print "cleaning up file"