from db import init_db
from datetime import datetime
import sqlite3

init_db()

def add_transaction(t_type, category, amount, comment=""):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    cursor.execute("INSERT INTO transactions (type, category, amount, date, comment) VALUES (?, ?, ?, ?, ?)",
                   (t_type, category, amount, date, comment))
    conn.commit()
    conn.close()

def get_balance():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='Доход'")
    income = cursor.fetchone()[0] or 0
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='Расход'")
    expense = cursor.fetchone()[0] or 0
    conn.close()
    return income - expense

# Тест
add_transaction("Доход", "Зарплата", 1500, "Сентябрь")
add_transaction("Расход", "Продукты", 300, "Супермаркет")

print("Текущий баланс:", get_balance())
