import pandas as pd
import matplotlib.pyplot as plt
from data_operations import get_all_data

def visualize_data():
    incomes, expenses = get_all_data()
    
    if incomes.empty and expenses.empty:
        print("No data available to visualize.")
        return

    # Convert date columns to datetime
    if not incomes.empty:
        incomes['date'] = pd.to_datetime(incomes['date'])
    
    if not expenses.empty:
        expenses['date'] = pd.to_datetime(expenses['date'])

    plt.figure(figsize=(10, 5))
    
    if not incomes.empty:
        plt.subplot(1, 2, 1)
        incomes.groupby(incomes['date'].dt.to_period('M'))['amount'].sum().plot(kind='bar', title='Monthly Income')
        plt.ylabel('Amount')
    
    if not expenses.empty:
        plt.subplot(1, 2, 2)
        expenses.groupby(expenses['date'].dt.to_period('M'))['amount'].sum().plot(kind='bar', title='Monthly Expenses')
        plt.ylabel('Amount')
    
    if not incomes.empty or not expenses.empty:
        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    visualize_data()