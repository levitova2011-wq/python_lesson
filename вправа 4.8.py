from tkinter import *
root = Tk()
root.geometry('300x400')
label1 = Label(text='Кількість етапів')
label1.pack(pady=10)
entry1 = Entry(width=20)
entry1.pack(pady=5)
label2 = Label(text='Довжина I етапу')
label2.pack(pady=10)
entry2 = Entry(width=20)
entry2.pack(pady=5)
def click():
    n = int(entry1.get())
    x = int(entry2.get())
    s = 0
    for i in range(n):
        s = s + x
        x = x + 30
    entry3.delete(0, END)
    entry3.insert(0, str(s))
button = Button(text='Обчислити', command=click)
button.pack(pady=10)
label3 = Label(text='Довжина велопробігу')
label3.pack(pady=5)
entry3 = Entry(width=20)
entry3.pack(pady=10)
root.mainloop()