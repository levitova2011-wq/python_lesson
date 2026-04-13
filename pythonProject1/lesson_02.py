from random import *
class Student:
    def __init__(self,name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 2
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <=0:
            print("Depression")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness is {self.gladness}")
        print(f"Progress is {self.progress}")