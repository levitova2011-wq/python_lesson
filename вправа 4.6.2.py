from tkinter import *
root = Tk()
entry_x = Entry(width=10)
entry_x.place(x=20, y=30)
entry_y = Entry(width=10)
entry_y.place(x=20, y=50)
def click():
    x = float(entry_x.get())
    if x ** 2 - 25 == 0:
        y = '∞'
    else:
        y = (x ** 2 - 4) / (x ** 2 - 25)
    entry_y.delete(0, END)
    entry_y.insert(0, str(y))
button = Button(width=10, text='Знайти', command=click)
button.place(x=20, y=80)
root.mainloop()
