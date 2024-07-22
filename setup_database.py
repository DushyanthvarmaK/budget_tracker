import sqlite3

def create_tables():
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()

    # Create Categories table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Categories (
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        type TEXT CHECK(type IN ('income', 'expense'))
    )
    ''')

    # Create Income table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Income (
        income_id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        date DATE NOT NULL,
        category_id INTEGER,
        description TEXT,
        FOREIGN KEY (category_id) REFERENCES Categories(category_id)
    )
    ''')

    # Create Expenses table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Expenses (
        expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        date DATE NOT NULL,
        category_id INTEGER,
        description TEXT,
        FOREIGN KEY (category_id) REFERENCES Categories(category_id)
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()