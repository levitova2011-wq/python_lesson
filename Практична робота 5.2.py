from tkinter import *
root = Tk()
root.geometry('300x250')
root.title('Калькулятор знижок')
entry = Entry(width=20)
entry.pack(pady=10)
def click():
    s = float(entry.get())
    if s < 500:
        discount = 0
    elif s <= 1000:
        discount = 0.05
    else:
        discount = 0.1
    result = s - s * discount
    label2.config(text=f'Знижка: {discount * 100}%')
    label1.config(text=f'До сплати: {result} грн')
button = Button(text='Обчислити', command=click)
button.pack(pady=10)
label1 = Label(text='')
label1.pack(pady=5)
label2 = Label(text='')
label2.pack(pady=5)
root.mainloop()