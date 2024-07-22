import sqlite3
import pandas as pd

# Existing functions...

def insert_income(amount, date, category_id, description):
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Income (amount, date, category_id, description)
        VALUES (?, ?, ?, ?)
    ''', (amount, date, category_id, description))
    conn.commit()
    conn.close()

def insert_expense(amount, date, category_id, description):
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Expenses (amount, date, category_id, description)
        VALUES (?, ?, ?, ?)
    ''', (amount, date, category_id, description))
    conn.commit()
    conn.close()

def insert_category(name, type):
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Categories (name, type)
        VALUES (?, ?)
    ''', (name, type))
    conn.commit()
    conn.close()

def get_categories():
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Categories')
    categories = cursor.fetchall()
    conn.close()
    return categories

def get_incomes():
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Income')
    incomes = cursor.fetchall()
    conn.close()
    return incomes

def get_expenses():
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Expenses')
    expenses = cursor.fetchall()
    conn.close()
    return expenses

def get_all_data():
    conn = sqlite3.connect('finance_tracker.db')
    incomes = pd.read_sql_query('SELECT * FROM Income', conn)
    expenses = pd.read_sql_query('SELECT * FROM Expenses', conn)
    conn.close()
    return incomes, expenses

def delete_income(income_id):
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Income WHERE income_id = ?', (income_id,))
    conn.commit()
    conn.close()

def delete_expense(expense_id):
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Expenses WHERE expense_id = ?', (expense_id,))
    conn.commit()
    conn.close()

def delete_category(category_id):
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Categories WHERE category_id = ?', (category_id,))
    conn.commit()
    conn.close()