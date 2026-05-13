import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

conn = sqlite3.connect("finance_manager.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS transactions")

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    category TEXT,
    amount REAL
)
""")

conn.commit()

class Transaction:
    def __init__(self, t_type, category, amount):
        self.t_type = t_type
        self.category = category
        self.amount = amount

    def save_to_db(self):
        cursor.execute(
            "INSERT INTO transactions (type, category, amount) VALUES (?, ?, ?)",
            (self.t_type, self.category, self.amount)
        )
        conn.commit()

class Category:
    def __init__(self, name):
        self.name = name

class FinanceManager:

    @staticmethod
    def get_balance():
        cursor.execute("""
        SELECT 
            SUM(CASE WHEN type='Доход' THEN amount ELSE 0 END) -
            SUM(CASE WHEN type='Расход' THEN amount ELSE 0 END)
        FROM transactions
        """)

        result = cursor.fetchone()[0]

        if result is None:
            return 0

        return result

    @staticmethod
    def get_transactions():
        cursor.execute("SELECT type, category, amount FROM transactions")
        return cursor.fetchall()

root = tk.Tk()
root.title("Менеджер личных финансов")
root.geometry("542x520")
root.configure(bg="#f0f4f8")

title = tk.Label(
    root,
    text="Менеджер личных финансов",
    font=("Arial", 20, "bold"),
    bg="#f0f4f8",
    fg="#1e3a5f"
)
title.grid(pady=10)

frame = tk.Frame(root, bg="#f0f4f8")
frame.grid(pady=10)

tk.Label(frame, text="Тип:", bg="#f0f4f8", font=("Arial", 11)).grid(row=0, column=0, padx=5, pady=5)

type_var = tk.StringVar()
type_combo = ttk.Combobox(
    frame,
    textvariable=type_var,
    values=["Доход", "Расход"],
    state="readonly",
    width=15
)
type_combo.grid(row=0, column=1, padx=5)
type_combo.current(0)

tk.Label(frame, text="Категория:", bg="#f0f4f8", font=("Arial", 11)).grid(row=1, column=0, padx=5, pady=5)

category_entry = tk.Entry(frame, width=20)
category_entry.grid(row=1, column=1)

tk.Label(frame, text="Сумма:", bg="#f0f4f8", font=("Arial", 11)).grid(row=2, column=0, padx=5, pady=5)

amount_entry = tk.Entry(frame, width=20)
amount_entry.grid(row=2, column=1)

columns = ("Тип", "Категория", "Сумма")

tree = ttk.Treeview(root, columns=columns, show="headings", height=12)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=180)

tree.grid(pady=10)

def refresh_table():
    for row in tree.get_children():
        tree.delete(row)

    transactions = FinanceManager.get_transactions()

    for transaction in transactions:
        tree.insert("", tk.END, values=transaction)

def add_transaction():
    t_type = type_var.get()
    category = category_entry.get().strip()
    amount = amount_entry.get()

    if t_type == "Доход":
        amount = f"+{amount}"
    else:
        amount = f"-{amount}"

    if category == "":
        category = "---"

    if not amount:
        messagebox.showerror("Ошибка", "Заполните все поля")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректную сумму")
        return

    category_obj = Category(category)

    transaction = Transaction(
        t_type,
        category_obj.name,
        amount
    )

    transaction.save_to_db()

    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

    refresh_table()

    global result_amount
    result_amount += amount

result_amount = 0
general_result_amount = 0
def result():
    global result_amount
    global general_result_amount
    category = "---"
    t_type = "ИТОГ"
    amount = result_amount
    category_obj = Category(category)
    transaction = Transaction(
        t_type,
        category_obj.name,
        amount
    )

    transaction.save_to_db()

    refresh_table()

    general_result_amount += result_amount
    result_amount = 0


def general_result():
    global general_result_amount
    category = "---"
    t_type = "ОБЩИЙ ИТОГ"
    amount = general_result_amount
    category_obj = Category(category)
    transaction = Transaction(
        t_type,
        category_obj.name,
        amount
    )

    transaction.save_to_db()

    refresh_table()

button_frame = tk.Frame(root)
button_frame.grid(pady=10)

button1 = tk.Button(
    button_frame,
    text="Добавить операцию",
    command=add_transaction,
    bg="#2563eb",
    fg="white",
    font=("Arial", 11, "bold"),

)

button1.grid(row=3, column=0, padx=5)

button2 = tk.Button(
    button_frame,
    text="Итог",
    command=result,
    bg="red",
    fg="white",
    font=("Arial", 11, "bold"),
)

button2.grid(row=3, column=1, padx=5)

button3 = tk.Button(
    button_frame,
    text="Общий итог",
    command=general_result,
    bg="red",
    fg="white",
    font=("Arial", 11, "bold"),
)

button3.grid(row=3, column=2, padx=5)

refresh_table()

root.mainloop()

conn.close()
