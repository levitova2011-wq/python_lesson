from random import *
class Animal:
    def __init__(self,name):
        self.name = name
        self.dog_energy = 100
        self.cat_energy = 100
        self.bird_energy = 100
        self.alive = True
        self.animal = "dog"
    def eat(self):
        print("Eat time!")
        if self.animal == "dog":
            self.dog_energy += 10
        elif self.animal == "cat":
            self.cat_energy += 10
        else:
            self.bird_energy += 10
    def sleep(self):
        print("Time to sleep!")
        if self.animal == "dog":
            self.dog_energy += 3 + round((100 - self.dog_energy)*0.25)
        elif self.animal == "cat":
            self.cat_energy += 3 + round((100 - self.cat_energy)*0.25)
        else:
            self.bird_energy += 3 + round((100 - self.bird_energy)*0.25)
    def speak(self):
        if self.animal == "dog":
            print("Woof-woof")
        elif self.animal == "cat":
            print("Meow")
        else:
            print("Tweet-tweet")
    def fetch(self):
        print("Fetching")
        self.dog_energy -= 15
    def scratch(self):
        print("Scratching")
        self.cat_energy -= 15
    def fly(self):
        print("Flying")
        self.bird_energy -= 15
    def do(self):
        if self.animal == "dog":
            self.fetch()
        elif self.animal == "cat":
            self.scratch()
        else:
            self.fly()
    def is_alive(self):
        if self.dog_energy <= 0:
            print("Dog is so tired...")
            self.alive = False
        elif self.cat_energy <= 0:
            print("Cat is so tired...")
            self.alive = False
        elif self.bird_energy <= 0:
            print("Bird is so tired...")
            self.alive = False
    def end_of_day(self):
        print(f"Dog energy is: {self.dog_energy}")
        print(f"Cat energy is: {self.cat_energy}")
        print(f"Bird energy is: {self.bird_energy}")
    def live(self,day):
        print(f"day is {day}")
        live_cube = randint(1,4)
        self.animal = "dog"
        print("Dog:")
        if live_cube == 1:
            self.eat()
        elif live_cube == 2:
            self.sleep()
        elif live_cube == 3:
            self.speak()
        else:
            self.fetch()
        live_cube = randint(1, 4)
        self.animal = "cat"
        print("Cat:")
        if live_cube == 1:
            self.eat()
        elif live_cube == 2:
            self.sleep()
        elif live_cube == 3:
            self.speak()
        else:
            self.scratch()
        live_cube = randint(1, 4)
        self.animal = "bird"
        print("Bird:")
        if live_cube == 1:
            self.eat()
        elif live_cube == 2:
            self.sleep()
        elif live_cube == 3:
            self.speak()
        else:
            self.fly()
        if self.dog_energy > 100:
            self.dog_energy = 100
        if self.cat_energy > 100:
            self.cat_energy = 100
        if self.bird_energy > 100:
            self.bird_energy = 100
        self.end_of_day()
        self.is_alive()
zoo = Animal("David")
for day in range(365):
    if zoo.alive == False:
        break
    else:
        zoo.live(day)