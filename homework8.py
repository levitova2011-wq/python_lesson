import tkinter as tk

hp = 100
time = 0
press_return = True

def start(event):
    global press_return
    if not press_return:
        pass
    else:
        label.config(text='')
        update_bomb()
        update_score()
        update_display()
        press_return = False


def update_display():
    global hp
    global time
    if hp >= 70:
        bomb_label.config(image=img_1)
    elif 30 <= hp < 70:
        bomb_label.config(image=img_2)
    elif 0 < hp < 30:
        bomb_label.config(image=img_3)
    else:
        bomb_label.config(image=img_4)
    fuse_label.config(text='HP: ' + str(hp))
    score_label.config(text='Time: ' + str(time))
    fuse_label.after(100, update_display)



def update_bomb():
    global hp
    if 0 != hp < 100:
        hp += 1
    if is_alive():
        fuse_label.after(300, update_bomb)


def update_score():
    global time
    if is_alive():
        time += 0.01
        time = round(time, 3)
        score_label.after(10, update_score)


def click():
    global hp
    if is_alive():
        hp -= 1


def is_alive():
    global hp
    global press_return
    if hp <= 0:
        hp = 0
        label.config(text='Well done!')
        press_return = True
        return False
    else:
        return True


root = tk.Tk()
root.title('Kill the beetle!')
root.geometry('1000x1000')
root.iconbitmap("bomb.ico")


label = tk.Label(root, text='Press [enter] to start the game', font=('Comic Sans MS', 12))
label.pack()

fuse_label = tk.Label(root, text='HP: ' + str(time), font=('Comic Sans MS', 14))
fuse_label.pack()

score_label = tk.Label(root, text='Time: ' + str(time), font=('Comic Sans MS', 14))
score_label.pack()
click_button = tk.Button(root, text='Click me', bg='#000000', fg='#ffffff', width=15, font=('Comic Sans MS', 14), command=click)
click_button.pack()
img_1 = tk.PhotoImage(file="1.gif")
img_2 = tk.PhotoImage(file="2.gif")
img_3 = tk.PhotoImage(file="3.gif")
img_4 = tk.PhotoImage(file="4.gif")       

bomb_label = tk.Label(root, image=img_1)
bomb_label.pack()



root.bind('<Return>', start)
root.mainloop()