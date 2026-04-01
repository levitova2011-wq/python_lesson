from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('500x500')
def click1():
    h = int(entry1.get())
    p = int(entry2.get())
    n = int(entry3.get())
    result = h
    for i in range(n):
        result += p
    entry4.delete(0, END)
    entry4.insert(0, f'Через {n} годин рівень води у річці буде: {result} см')
def click2():
    h = int(entry1.get())
    p = int(entry2.get())
    k = int(entry5.get())
    result = h
    n = 0
    while result < k:
        result += p
        n += 1
    messagebox.showinfo(f'Кількість годин {n}', f'Через {n} годин рівень води в річці буде не менше {k} см')
label1 = Label(text='Початковий рівень води h')
label1.pack(pady=10)
entry1 = Entry(width=10)
entry1.pack(pady=5)
label2 = Label(text='Зростання рівня води p')
label2.pack(pady=10)
entry2 = Entry(width=10)
entry2.pack(pady=5)
label3 = Label(text='Тривалість повені n')
label3.pack(pady=10)
entry3 = Entry(width=10)
entry3.pack(pady=5)
button1 = Button(text='Запитання №1', command=click1)
button1.pack(pady=10)
entry4 = Entry(width=50)
entry4.pack(pady=5)
label4 = Label(text='Рівень води K')
label4.pack(pady=10)
entry5 = Entry(width=10)
entry5.pack(pady=5)
button2 = Button(text='Запитання №2', command=click2)
button2.pack(pady=10)
root.mainloop()