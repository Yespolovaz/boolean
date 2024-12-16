import tkinter as tk
from tkinter import ttk, messagebox
from general import QuineMcCluskey

class QuineMcCluskeyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quine-McCluskey Minimization")
        self.root.config(bg="#2c503b")  
        
        self.label = ttk.Label(root, text="Enter Minterms (space-separated):", foreground="#ffffff", background="#2c503b")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.minterm_entry = ttk.Entry(root, width=50)
        self.minterm_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        button_style = ttk.Style()
        button_style.configure("TButton", padding=10, relief="flat", background="#87eaa8", foreground="#2c3e50", width=20)

        self.process_button = ttk.Button(root, text="Process", command=self.process_minterms, style="TButton")
        self.process_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.clear_button = ttk.Button(root, text="Clear", command=self.clear_fields, style="TButton")
        self.clear_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.output_text = tk.Text(root, width=80, height=30, wrap=tk.WORD, bg="#e4fdf4", fg="#2c503b")
        self.output_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def process_minterms(self):
        minterms = self.minterm_entry.get()
        try:
            qm = QuineMcCluskey(minterms)
            output = qm.table()
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, output)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def clear_fields(self):
        self.minterm_entry.delete(0, tk.END)
        self.output_text.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuineMcCluskeyGUI(root)
    root.mainloop()
