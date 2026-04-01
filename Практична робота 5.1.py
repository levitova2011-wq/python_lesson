from tkinter import *
root = Tk()
root.geometry('300x250')
root.title('Перевірка пароля')
label = Label(text='')
label.pack(pady=10)
entry = Entry(width=16)
entry.pack(pady=2)
def click():
    if entry.get() == 'admin123':
        label.config(text='Доступ дозволено', fg='green')
    else:
        label.config(text='Доступ заборонено', fg='red')
button = Button(text='Перевірити', command=click)
button.pack(pady=10)
root.mainloop()