from tkinter import *
root = Tk()
root.geometry('400x200')
entry = Entry(width=15, bd=3)
entry.pack(padx=0, pady=40)
button = Button(width=10, text='8-Б клас', fg='blue', bg='yellow')
button.pack(padx=30, pady=0)
def click():
    entry.config(bg='red', font=('Arial', 14), width=35, fg='white')
    entry.delete(0, END)
    entry.insert(0, 'Ми використовуємо властивості поля!')
button.config(command=click)
root.mainloop()
