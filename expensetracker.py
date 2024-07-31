import tkinter as tk
from tkinter import messagebox

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("400x400")

        self.expenses = []

        self.create_widgets()

    def create_widgets(self):
        self.desc_label = tk.Label(self.root, text="Description")
        self.desc_label.pack()
        self.desc_entry = tk.Entry(self.root, width=50)
        self.desc_entry.pack(pady=5)

        self.amount_label = tk.Label(self.root, text="Amount")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self.root, width=50)
        self.amount_entry.pack(pady=5)

        self.category_label = tk.Label(self.root, text="Category")
        self.category_label.pack()
        self.category_entry = tk.Entry(self.root, width=50)
        self.category_entry.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Add Expense", command=self.add_expense)
        self.add_button.pack(pady=5)

        self.expense_listbox = tk.Listbox(self.root, width=50, height=10)
        self.expense_listbox.pack(pady=10)

        self.remove_button = tk.Button(self.root, text="Remove Expense", command=self.remove_expense)
        self.remove_button.pack(pady=5)

        self.total_button = tk.Button(self.root, text="View Total Expenses", command=self.view_total_expenses)
        self.total_button.pack(pady=5)

    def add_expense(self):
        pass

    def remove_expense(self):
        pass

    def view_total_expenses(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
