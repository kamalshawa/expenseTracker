import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from models import Expense

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("400x500")

        self.expenses = []

        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        list_frame = tk.Frame(self.root)
        list_frame.pack(pady=10)

        filter_frame = tk.Frame(self.root)
        filter_frame.pack(pady=10)

        self.desc_label = tk.Label(input_frame, text="Description")
        self.desc_label.grid(row=0, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(input_frame, width=40)
        self.desc_entry.grid(row=0, column=1, padx=5, pady=5)

        self.amount_label = tk.Label(input_frame, text="Amount")
        self.amount_label.grid(row=1, column=0, padx=5, pady=5)
        self.amount_entry = tk.Entry(input_frame, width=40)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        self.category_label = tk.Label(input_frame, text="Category")
        self.category_label.grid(row=2, column=0, padx=5, pady=5)
        self.category_entry = tk.Entry(input_frame, width=40)
        self.category_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_button = tk.Button(button_frame, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.remove_button = tk.Button(button_frame, text="Remove Expense", command=self.remove_expense)
        self.remove_button.grid(row=0, column=1, padx=5, pady=5)

        self.total_button = tk.Button(button_frame, text="View Total Expenses", command=self.view_total_expenses)
        self.total_button.grid(row=0, column=2, padx=5, pady=5)

        self.expense_listbox = tk.Listbox(list_frame, width=50, height=10)
        self.expense_listbox.pack(pady=10)

        self.filter_label = tk.Label(filter_frame, text="Filter by Category")
        self.filter_label.grid(row=0, column=0, padx=5, pady=5)

        self.category_var = tk.StringVar()
        self.category_combobox = ttk.Combobox(filter_frame, textvariable=self.category_var)
        self.category_combobox['values'] = []  # Initialize with empty values
        self.category_combobox.grid(row=0, column=1, padx=5, pady=5)

        self.filter_button = tk.Button(filter_frame, text="Apply Filter", command=self.apply_filter)
        self.filter_button.grid(row=0, column=2, padx=5, pady=5)

        self.category_total_button = tk.Button(filter_frame, text="View Category Total",
                                               command=self.view_category_total)
        self.category_total_button.grid(row=0, column=3, padx=5, pady=5)

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
                self.update_category_combobox()
                self.desc_entry.delete(0, tk.END)
                self.amount_entry.delete(0, tk.END)
                self.category_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid amount.")
        else:
            messagebox.showwarning("Missing Fields", "Please fill in all fields.")

    def update_expense_listbox(self, category_filter=None):
        self.expense_listbox.delete(0, tk.END)
        for expense in self.expenses:
            if category_filter is None or expense.category == category_filter:
                self.expense_listbox.insert(tk.END, str(expense))

    def remove_expense(self):
        selected_index = self.expense_listbox.curselection()
        if selected_index:
            del self.expenses[selected_index[0]]
            self.update_expense_listbox()
            self.update_category_combobox()
        else:
            messagebox.showwarning("Warning", "No expense selected")

    def view_total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        messagebox.showinfo("Total Expenses", f"Total Expenses: ${total:.2f}")

    def update_category_combobox(self):
        categories = list(set(expense.category for expense in self.expenses))
        self.category_combobox['values'] = categories

    def apply_filter(self):
        selected_category = self.category_var.get()
        if selected_category:
            self.update_expense_listbox(category_filter=selected_category)
        else:
            self.update_expense_listbox()

    def view_category_total(self):
        selected_category = self.category_var.get()
        if selected_category:
            total = sum(expense.amount for expense in self.expenses if expense.category == selected_category)
            messagebox.showinfo("Category Total", f"Total Expenses for {selected_category}: ${total:.2f}")
        else:
            messagebox.showwarning("Warning", "No category selected")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
