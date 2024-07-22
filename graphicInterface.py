import tkinter as tk
from tkinter import messagebox
from data_operations import (
    insert_income, insert_expense, insert_category, 
    get_categories, get_incomes, get_expenses,
    delete_income, delete_expense, delete_category
)

def add_income():
    try:
        insert_income(float(amount_entry.get()), date_entry.get(), int(category_id_entry.get()), description_entry.get())
        messagebox.showinfo("Success", "Income added successfully")
        refresh_data()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def add_expense():
    try:
        insert_expense(float(amount_entry.get()), date_entry.get(), int(category_id_entry.get()), description_entry.get())
        messagebox.showinfo("Success", "Expense added successfully")
        refresh_data()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def add_category():
    try:
        insert_category(category_name_entry.get(), category_type_var.get())
        messagebox.showinfo("Success", "Category added successfully")
        refresh_categories()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_selected_income():
    try:
        selected_income = income_listbox.get(income_listbox.curselection())
        income_id = selected_income.split(':')[0]
        delete_income(income_id)
        messagebox.showinfo("Success", "Income deleted successfully")
        refresh_data()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_selected_expense():
    try:
        selected_expense = expense_listbox.get(expense_listbox.curselection())
        expense_id = selected_expense.split(':')[0]
        delete_expense(expense_id)
        messagebox.showinfo("Success", "Expense deleted successfully")
        refresh_data()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_selected_category():
    try:
        selected_category = categories_listbox.get(categories_listbox.curselection())
        category_id = selected_category.split(':')[0]
        delete_category(category_id)
        messagebox.showinfo("Success", "Category deleted successfully")
        refresh_categories()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def refresh_categories():
    categories = get_categories()
    categories_listbox.delete(0, tk.END)
    max_width = 0
    for category in categories:
        category_str = f"{category[0]}: {category[1]} ({category[2]})"
        categories_listbox.insert(tk.END, category_str)
        max_width = max(max_width, len(category_str))
    categories_listbox.config(width=max_width)

def refresh_data():
    incomes = get_incomes()
    expenses = get_expenses()
    
    income_listbox.delete(0, tk.END)
    max_income_width = 0
    for income in incomes:
        income_str = f"{income[0]}: {income[1]} on {income[2]} (Category: {income[3]}) - {income[4]}"
        income_listbox.insert(tk.END, income_str)
        max_income_width = max(max_income_width, len(income_str))
    income_listbox.config(width=max_income_width)
    
    expense_listbox.delete(0, tk.END)
    max_expense_width = 0
    for expense in expenses:
        expense_str = f"{expense[0]}: {expense[1]} on {expense[2]} (Category: {expense[3]}) - {expense[4]}"
        expense_listbox.insert(tk.END, expense_str)
        max_expense_width = max(max_expense_width, len(expense_str))
    expense_listbox.config(width=max_expense_width)

def _on_mouse_wheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# Create GUI
root = tk.Tk()
root.title("Finance Tracker")
root.geometry("500x600")

# Create a canvas and a scrollbar
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Bind mouse wheel to canvas
canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

# Add widgets to scrollable frame
tk.Label(scrollable_frame, text="Amount:").pack()
amount_entry = tk.Entry(scrollable_frame)
amount_entry.pack()

tk.Label(scrollable_frame, text="Date (YYYY-MM-DD):").pack()
date_entry = tk.Entry(scrollable_frame)
date_entry.pack()

tk.Label(scrollable_frame, text="Category ID:").pack()
category_id_entry = tk.Entry(scrollable_frame)
category_id_entry.pack()

tk.Label(scrollable_frame, text="Description:").pack()
description_entry = tk.Entry(scrollable_frame)
description_entry.pack()

tk.Button(scrollable_frame, text="Add Income", command=add_income).pack()
tk.Button(scrollable_frame, text="Add Expense", command=add_expense).pack()

# Category Inputs
tk.Label(scrollable_frame, text="Category Name:").pack()
category_name_entry = tk.Entry(scrollable_frame)
category_name_entry.pack()

category_type_var = tk.StringVar(value="income")
tk.Radiobutton(scrollable_frame, text="Income", variable=category_type_var, value="income").pack()
tk.Radiobutton(scrollable_frame, text="Expense", variable=category_type_var, value="expense").pack()

tk.Button(scrollable_frame, text="Add Category", command=add_category).pack()

# Category List
tk.Label(scrollable_frame, text="Categories:").pack()
categories_listbox = tk.Listbox(scrollable_frame)
categories_listbox.pack()

tk.Button(scrollable_frame, text="Delete Selected Category", command=delete_selected_category).pack()
tk.Button(scrollable_frame, text="Refresh Categories", command=refresh_categories).pack()

# Income List
tk.Label(scrollable_frame, text="Incomes:").pack()
income_listbox = tk.Listbox(scrollable_frame)
income_listbox.pack()

tk.Button(scrollable_frame, text="Delete Selected Income", command=delete_selected_income).pack()

# Expense List
tk.Label(scrollable_frame, text="Expenses:").pack()
expense_listbox = tk.Listbox(scrollable_frame)
expense_listbox.pack()

tk.Button(scrollable_frame, text="Delete Selected Expense", command=delete_selected_expense).pack()

tk.Button(scrollable_frame, text="Refresh Data", command=refresh_data).pack()

# Pack canvas and scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Initial refresh to display categories and data
refresh_categories()
refresh_data()

root.mainloop()