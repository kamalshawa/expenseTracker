import tkinter as tk
from tkinter import messagebox
from models import Expense

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("400x500")

        self.expenses = []

        self.create_widgets()

    def create_widgets(self):
        self.desc_label = tk.Label(self.root, text="Description")
        self.desc_label.pack(pady=5)
        self.desc_entry = tk.Entry(self.root, width=50)
        self.desc_entry.pack(pady=5)

        self.amount_label = tk.Label(self.root, text="Amount")
        self.amount_label.pack(pady=5)
        self.amount_entry = tk.Entry(self.root, width=50)
        self.amount_entry.pack(pady=5)

        self.category_label = tk.Label(self.root, text="Category")
        self.category_label.pack(pady=5)
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
        description = self.desc_entry.get()
        amount = self.amount_entry.get()
        category = self.category_entry.get()
        if description and amount and category:
            try:
                amount = float(amount)
                expense = Expense(description, amount, category)
                self.expenses.append(expense)
                self.update_expense_listbox()
                self.desc_entry.delete(0, tk.END)
                self.amount_entry.delete(0, tk.END)
                self.category_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid amount.")
        else:
            messagebox.showwarning("Missing Fields", "Please fill in all fields.")

    def update_expense_listbox(self):
        self.expense_listbox.delete(0, tk.END)
        for expense in self.expenses:
            self.expense_listbox.insert(tk.END, str(expense))

    def remove_expense(self):
        selected_index = self.expense_listbox.curselection()
        if selected_index:
            del self.expenses[selected_index[0]]
            self.update_expense_listbox()
        else:
            messagebox.showwarning("Warning", "No expense selected")

    def view_total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        messagebox.showinfo("Total Expenses", f"Total Expenses: ${total:.2f}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
