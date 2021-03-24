# Python program showing
# abstract base class work

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def move(self):
        pass


class Human(Animal):

    def move(self):
        print("I can walk and run")

    def move1(self):
        print("I can walk and runnnnnn")


class Snake(Animal):

    def move(self):
        print("I can crawl")


class Dog(Animal):

    def move(self):
        print("I can bark")


class Lion(Animal):

    def move(self):
        print("I can roar")

    # Driver code


R = Human()
R.move1()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()
