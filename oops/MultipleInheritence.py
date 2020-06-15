class Father:
    def skills(self):
        print "Father : Programming, Gardening"
class Mother:
    def skills(self):
        print "Mother : Singing, Cooking"
class Child(Father,Mother):
    def skills(self):
        Father.skills(self)                                 #inheritence from Father class
        Mother.skills(self)                                 #inheritence from child class
        print "Child : Painting, Sports"
if __name__=="__main__":
        c= Child()
        c.skills()