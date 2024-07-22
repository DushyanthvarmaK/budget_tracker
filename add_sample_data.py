import sqlite3

def add_sample_data():
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()

    # Insert sample categories
    cursor.execute('INSERT INTO Categories (name, type) VALUES (?, ?)', ('Salary', 'income'))
    cursor.execute('INSERT INTO Categories (name, type) VALUES (?, ?)', ('Groceries', 'expense'))
    
    # Get the IDs of the inserted categories
    cursor.execute('SELECT category_id FROM Categories WHERE name = ?', ('Salary',))
    salary_id = cursor.fetchone()[0]
    
    cursor.execute('SELECT category_id FROM Categories WHERE name = ?', ('Groceries',))
    groceries_id = cursor.fetchone()[0]
    
    # Insert sample incomes
    cursor.execute('INSERT INTO Income (amount, date, category_id, description) VALUES (?, ?, ?, ?)',
                   (1000.00, '2024-07-22', salary_id, 'Monthly salary'))
    
    # Insert sample expenses
    cursor.execute('INSERT INTO Expenses (amount, date, category_id, description) VALUES (?, ?, ?, ?)',
                   (200.00, '2024-07-22', groceries_id, 'Grocery shopping'))
    
    conn.commit()
    conn.close()
    print("Sample data added successfully.")

if __name__ == '__main__':
    add_sample_data()