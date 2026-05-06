import tkinter as tk
from random import *
class MoodGenerator:
    def __init__(self, root):
        self.mood = ""
        self.root = root
        self.label1 = tk.Label(root, text="Your mood:")
        self.label1.pack()
        self.label2 = tk.Label(root, text="")
        self.label2.pack()
        tk.Button(root, text="Generate", command=self.get_mood).pack()
    def get_mood(self):
        randmood = randint(1, 4)
        if randmood == 1:
            self.mood = "cool"
        elif randmood == 2:
            self.mood = "sleepy"
        elif randmood == 3:
            self.mood = "motivated"
        else:
            self.mood = "surprised"
        self.label2.config(text=self.get_info())
    def get_info(self):
        return f"{self.mood}"

root = tk.Tk()
app = MoodGenerator(root)
root.mainloop()