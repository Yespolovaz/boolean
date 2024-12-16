import tkinter as tk
from tkinter import messagebox
from general import print_truth_table

class TruthTableGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Truth Table Generator")
        self.root.config(bg="#2c503b")

        self.variables_label = tk.Label(root, text="Variables (comma-separated):", foreground="#ffffff", background="#2c503b")
        self.variables_label.grid(row=0, column=0, padx=10, pady=5)
        self.variables_entry = tk.Entry(root)
        self.variables_entry.grid(row=0, column=1, padx=10, pady=5)

        self.columns_label = tk.Label(root, text="Column Names (comma-separated):", foreground="#ffffff", background="#2c503b")
        self.columns_label.grid(row=1, column=0, padx=10, pady=5)
        self.columns_entry = tk.Entry(root)
        self.columns_entry.grid(row=1, column=1, padx=10, pady=5)

        self.operations_label = tk.Label(root, text="Operations (dot-separated):", foreground="#ffffff", background="#2c503b")
        self.operations_label.grid(row=2, column=0, padx=10, pady=5)
        self.operations_entry = tk.Entry(root)
        self.operations_entry.grid(row=2, column=1, padx=10, pady=5)

        self.generate_button = tk.Button(root, text="Generate Table", command=self.generate_table)
        self.generate_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.output_text = tk.Text(root, height=15, width=70)
        self.output_text.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    def generate_table(self):
        variables = self.variables_entry.get().split(',')
        columns_names = self.columns_entry.get().split(',')
        operations = self.operations_entry.get().split('.')

        try:
            columns = []
            for op in operations:
                op = op.strip()
                if op in ['and', 'or', 'not']:
                    columns.append(op)
                else:
                    columns.append(eval(op))

            result = print_truth_table(variables, columns, columns_names)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, result)

        except Exception as e:
            messagebox.showerror("Error", str(e))