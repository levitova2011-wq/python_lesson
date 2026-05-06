import tkinter as tk

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


    def add_score(self,amount):
        self.score += amount

    def get_info(self):
        return f"{self.name}: {self.score}"


class App:
    def __init__(self,root):
        self.root = root
        self.player = None

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.label = tk.Label(root,text="")
        self.label.pack()

        tk.Button(root,text="Створити",command=self.create_player).pack()
        tk.Button(root,text="Додати 10",command=self.add_score).pack()

    def create_player(self):
        name = self.entry.get()
        self.player = Player(name)
        self.label.config(text="Гравець створений")

    def add_score(self):

        if self.player:
            self.player.add_score(10)
            self.label.config(text=self.player.get_info())

root = tk.Tk()
app = App(root)

root.mainloop()