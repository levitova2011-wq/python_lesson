from tkinter import *
root = Tk()
root.geometry('300x400')
def click():
    x = float(entry1.get())
    p = float(entry2.get())
    a = float(entry3.get())
    n = 0
    while x < a:
        x += x*p/100
        n += 1
    entry4.delete(0, END)
    entry4.insert(0, str(n))
label1 = Label(text='Початкова сума')
label1.pack(pady=10)
entry1 = Entry()
entry1.pack(pady=5)
label2 = Label(text='Річні відсотки')
label2.pack(pady=10)
entry2 = Entry()
entry2.pack(pady=5)
label3 = Label(text='Кінцева сума')
label3.pack(pady=10)
entry3 = Entry()
entry3.pack(pady=5)
button = Button(text='Обчислити', command=click)
button.pack(pady=10)
label4 = Label(text='Кількість років')
label4.pack(pady=5)
entry4 = Entry()
entry4.pack(pady=10)
root.mainloop()