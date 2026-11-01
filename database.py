import sqlite3

def connect():
    return sqlite3.connect("expenses.db")


def create_table():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                category TEXT,
                amount REAL,
                description TEXT
            )
        """)


def add_expense(date, category, amount, description):
    with connect() as conn:
        conn.execute("""
            INSERT INTO expenses
            (date, category, amount, description)
            VALUES (?, ?, ?, ?)
        """, (date, category, amount, description))


def view_expenses():
    with connect() as conn:
        cursor = conn.execute("SELECT * FROM expenses")
        return cursor.fetchall()


def update_expense(expense_id, amount):
    with connect() as conn:
        conn.execute("""
            UPDATE expenses
            SET amount = ?
            WHERE id = ?
        """, (amount, expense_id))


def delete_expense(expense_id):
    with connect() as conn:
        conn.execute(
            "DELETE FROM expenses WHERE id = ?",
            (expense_id,)
        )
