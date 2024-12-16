import tkinter as tk
from tkinter import ttk
from tt_gui import TruthTableGUI
from mc_gui import QuineMcCluskeyGUI


class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Logic Tools Suite")
        self.root.geometry("450x250")
        self.root.config(bg="#2c503b")  

        ttk.Label(root, text="Welcome to the Logic Tools Suite!", font=("Times New Roman", 16, 'bold'), foreground="#ffffff", background="#2c503b").pack(pady=30)

        button_style = ttk.Style()
        button_style.configure("TButton", font=("Times New Roman", 12), padding=10, relief="flat", background="#87eaa8", foreground="#2c3e50", width=20)

        ttk.Button(root, text="Truth Table Generator", command=self.open_truth_table, style="TButton").pack(pady=10)
        ttk.Button(root, text="Quine-McCluskey Minimization", command=self.open_quine_mccluskey, style="TButton").pack(pady=10)
        ttk.Button(root, text="Exit", command=root.quit, style="TButton").pack(pady=20)

    def open_truth_table(self):
        self.new_window(TruthTableGUI, "Truth Table Generator")

    def open_quine_mccluskey(self):
        self.new_window(QuineMcCluskeyGUI, "Quine-McCluskey Minimization")

    def new_window(self, gui_class, title):
        new_win = tk.Toplevel(self.root)
        new_win.title(title)
        new_win.config(bg="#e4fdf4")  # Light green background for new window
        gui_class(new_win)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()
