import tkinter as tk
from tkinter import messagebox, Menu
from tkinter import ttk


def calculate(operation, num1, num2):
    """Custom function to perform calculations"""
    try:
        num1 = float(num1)
        num2 = float(num2)
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "×":
            return num1 * num2
        elif operation == "÷":
            return num1 / num2
    except ValueError:
        return "Invalid number"
    except ZeroDivisionError:
        return "Cannot divide by zero"


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Styled Calculator")

        # Configure style
        style = ttk.Style()
        style.theme_use('clam')

        # Menu bar
        menubar = Menu(root)
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Clear", command=self.clear_all)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        root.config(menu=menubar)

        # Main frame
        main = ttk.Frame(root, padding=10)
        main.grid(row=0, column=0, sticky="NSEW")

        # Entries and operator
        self.num1_entry = ttk.Entry(main, width=15)
        self.operator_var = tk.StringVar(value="+")
        self.operator_menu = ttk.Combobox(main, textvariable=self.operator_var, values=["+", "-", "×", "÷"], width=3, state="readonly")
        self.num2_entry = ttk.Entry(main, width=15)
        self.calc_button = ttk.Button(main, text="Calculate", command=self.show_result)

        self.num1_entry.grid(row=0, column=0, padx=5, pady=5)
        self.operator_menu.grid(row=0, column=1, padx=5)
        self.num2_entry.grid(row=0, column=2, padx=5)
        self.calc_button.grid(row=0, column=3, padx=5)

        # History listbox
        self.history = tk.Listbox(main, height=8)
        self.history.grid(row=1, column=0, columnspan=4, pady=(10,0), sticky="EW")

        # Allow resizing
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main.columnconfigure((0,1,2,3), weight=1)

    def show_result(self):
        op = self.operator_var.get()
        n1 = self.num1_entry.get()
        n2 = self.num2_entry.get()
        result = calculate(op, n1, n2)
        self.history.insert(tk.END, f"{n1} {op} {n2} = {result}")
        messagebox.showinfo("Result", f"{n1} {op} {n2} = {result}")

    def clear_all(self):
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.history.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()