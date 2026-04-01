from tkinter import *
root = Tk()
root.geometry('300x200')
root.title('Детектор чисел')
entry = Entry(width=20)
entry.pack(pady=10)
def click():
    n = int(entry.get())
    if n > 0:
        sign = 'Додатне'
    elif n < 0:
        sign = "Від'ємне"
    else:
        sign = 'Нуль'
    if n % 2 == 0:
        parity = 'Парне'
    else:
        parity = 'Непарне'
    label1.config(text=f'{sign}')
    label2.config(text=f'{parity}')
button = Button(text='Проаналізувати', command=click)
button.pack(pady=5)
label1 = Label(text='')
label1.pack(pady=10)
label2 = Label(text='')
label2.pack(pady=5)
root.mainloop()