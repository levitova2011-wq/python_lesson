from random import *
class Gamer:
    def __init__(self,name):
        self.name = name
        self.energy = 50
        self.skill = 0
        self.mood = 50
        self.alive = True
    def play(self):
        print("Playing games...")
        random_event = randint(1, 5)
        if random_event <= 3:
            if randint(1, 50) < 50:
                print("Nothing special...")
                self.skill += 0.15
                self.energy -= 5
                self.mood += 2
            else:
                print("Won tournament...")
                self.skill += 3
                self.mood += 100
        elif random_event == 2:
            print("Internet lost...")
            self.mood -= 25
        else:
            print("Bad randoms...")
            self.mood -= 30
            self.energy -= 5
    def sleep(self):
        print("Sleeping...")
        self.energy += 10
        self.mood += 1
    def eat(self):
        print("Eating...")
        self.energy += 3
        self.mood += 3
    def stream(self):
        print("Streaming...")
        self.skill += 0.35
        self.energy -= 10
        self.mood += 8
    def is_alive(self):
        if self.energy <= 0:
            print("Burned out...")
            self.alive = False
        elif self.mood <= 0:
            print("Tilted...")
            self.alive = False
        elif self.skill >= 5:
            print("Pro player now!")
            self.alive = False
    def end_of_day(self):
        print(f"Energy: {self.energy}")
        print(f"Mood: {self.mood}")
        print(f"Skill: {round(self.skill)}")
    def live(self,day):
        print(f"day is {day}")
        live_cube = randint(1,4)
        if live_cube == 1:
            self.play()
        elif live_cube == 2:
            self.sleep()
        elif live_cube == 3:
            self.eat()
        elif live_cube == 4:
            self.stream()

        self.end_of_day()
        self.is_alive()

max_gamer = Gamer("Sasha")

for day in range(365):
    if max_gamer.alive == False:
        break
    else:
        max_gamer.live(day)