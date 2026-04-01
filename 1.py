from tkinter import *
root = Tk()
entry1 = Entry(width=10)
entry1.place(x=10, y=5)
entry2 = Entry(width=10)
entry2.place(x=10, y=25)
entry3 = Entry(width=10)
entry3.place(x=10, y=80)
def click():
    x = float(entry1.get())
    y = float(entry2.get())
    z = x-y
    entry3.delete(0, END)
    entry3.insert(0, str(z))
button = Button(width=10, text='Обчислити', command=click)
button.place(x=5, y=50)
root.mainloop()