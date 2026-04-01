from tkinter import *
root = Tk()
root.geometry('400x100')
start_width = 15
def increase_width(event):
    current_width = button.cget('width')
    new_width = current_width + 5
    if new_width > 50:
        new_width = start_width
    button.config(width=new_width)
button = Button(width=start_width)
button.place(x=10, y=30)
button.bind('<Motion>', increase_width)
root.mainloop()