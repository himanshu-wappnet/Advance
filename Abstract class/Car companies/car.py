#we are using ABC module as decorating method of the base class as abstract.

from abc import ABC, abstractmethod

#Abstract Class created.

class Car():
    @abstractmethod #this decorater is used to create abstract method.
    def car(self):
        print("\n")
        print("-------------:The below are spec of car:------------")
        print("\n")