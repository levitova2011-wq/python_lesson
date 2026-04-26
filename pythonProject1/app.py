import sqlite3
conn = sqlite3.connect("my_db.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS workers")
cursor.execute("""
CREATE TABLE IF NOT EXISTS workers (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT UNIQUE NOT NULL,
age INTEGER NOT NULL CHECK (age >= 0 AND age <= 100),
salary INTEGER NOT NULL DEFAULT 1000
)
""")
cursor.execute("INSERT INTO workers (name, age, salary) VALUES (?,?,?)",
               ("David", 27, 1120)
               )
conn.commit()
cursor.execute("INSERT INTO workers (name, age, salary) VALUES (?,?,?)",
               ("Maks", 40, 1570)
               )
conn.commit()
cursor.execute("INSERT INTO workers (name, age) VALUES (?,?)",
               ("Vlad", 20)
               )
conn.commit()
cursor.execute("SELECT * FROM workers")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.execute("""
UPDATE workers
SET salary = ?
WHERE name = ?""",
               (1450, "maks"))
conn.commit()
cursor.execute("DELETE FROM workers WHERE id = ?", (1,))
conn.commit()
cursor.execute("SELECT * FROM workers")
rows = cursor.fetchall()
for row in rows:
    print(row)
add_worker = str(input("Add a new worker?\nYes/No: "))
while add_worker == "Yes":
    cursor.execute("INSERT INTO workers (name, age, salary) VALUES (?,?,?)",
                       (str(input("Name: ")), int(input("Age: ")), int(input("Salary: "))))
    conn.commit()
    add_worker = str(input("Add a new worker?\nYes/No: "))
    if add_worker == "No":
        cursor.execute("SELECT * FROM workers")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        break