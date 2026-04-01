from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('300x200')
label1 = Label(text='Всього грошей:').place(x=15, y=20)
label2 = Label(text='Вартість печива:').place(x=15, y=50)
label3 = Label(text='Вартість молока:').place(x=15, y=80)
label4 = Label(text='Вартість хліба:').place(x=15, y=110)
label1_1 = Label(text='грн').place(x=235, y=20)
label2_1 = Label(text='грн/100г').place(x=237, y=50)
label3_1 = Label(text='грн/л').place(x=240, y=80)
label4_1 = Label(text='грн').place(x=226, y=110)
entry1 = Entry(width=20)
entry1.place(x=110, y=20)
entry2 = Entry(width=20)
entry2.place(x=113, y=50)
entry3 = Entry(width=20)
entry3.place(x=116, y=80)
entry4 = Entry(width=20)
entry4.place(x=102, y=110)
def click():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        c = float(entry3.get())
        d = float(entry4.get())
        result = a-(b*4+c*2+d)
        if result >= 0:
            messagebox.showinfo("Залишилося:", str(result))
        else:
            messagebox.showwarning('Недостатньо коштів!')
    except ValueError:
        messagebox.showerror('Введіть числа!')
button = Button(width=15, text='Знайти', command=click).place(x=100, y=150)
root.mainloop()
