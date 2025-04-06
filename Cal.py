import tkinter as tk
from tkinter import messagebox

def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        messagebox.showerror("Fehler", "Ungültige Eingabe")

def clear_entry():
    entry.delete(0, tk.END)

def append_to_entry(text):
    entry.insert(tk.END, text)

root = tk.Tk()
root.title("Taschenrechner")
root.geometry("350x500")
root.configure(bg="#1E1E1E")

tk.Label(root, text="Taschenrechner", font=("Arial", 20, "bold"), bg="#1E1E1E", fg="#F1C40F").pack(pady=10)

entry = tk.Entry(root, font=("Arial", 22), justify='right', bg="#333333", fg="#F1C40F", bd=5, relief=tk.FLAT)
entry.pack(fill=tk.BOTH, padx=10, pady=10)

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+"),
    ("C",)
]

frame = tk.Frame(root, bg="#1E1E1E")
frame.pack(expand=True, fill=tk.BOTH)

def create_round_button(frame, text, command, row, column):
    canvas = tk.Canvas(frame, width=70, height=70, bg="#1E1E1E", highlightthickness=0)
    canvas.grid(row=row, column=column, padx=5, pady=5)
    canvas.create_oval(5, 5, 65, 65, fill="#F39C12", outline="#F39C12")
    canvas.create_text(35, 35, text=text, font=("Arial", 18, "bold"), fill="black")
    canvas.bind("<Button-1>", lambda event: command())

for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        action = evaluate_expression if btn_text == "=" else clear_entry if btn_text == "C" else lambda t=btn_text: append_to_entry(t)
        create_round_button(frame, btn_text, action, i, j)

for i in range(len(buttons)):
    frame.grid_rowconfigure(i, weight=1)
for j in range(len(buttons[0])):
    frame.grid_columnconfigure(j, weight=1)

root.mainloop()
