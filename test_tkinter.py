import tkinter as tk

root = tk.Tk()
root.title("Test Tkinter")
root.geometry("300x200")

label = tk.Label(root, text="Tkinter is working!")
label.pack(pady=20)

root.mainloop()