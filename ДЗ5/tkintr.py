import tkinter as tk
from tkinter import messagebox

def v():
    try:
        x = float(b.get())
        y = float(d.get())
    except ValueError:
        messagebox.showwarning("Сбой", "Только цифры!")
        return

    if x <= 0 or y <= 0:
        messagebox.showwarning("Сбой", "Больше нуля!")
        return

    z = x * y if p.get() == "Прямоугольник" else 0.5 * x * y
    g.config(text=f"Итог: {z:.2f}")
    messagebox.showinfo("Ок", "Готово!")

w = tk.Tk()
w.title("Счет")

a = tk.Label(w, text="A:")
b = tk.Entry(w)
c = tk.Label(w, text="B:")
d = tk.Entry(w)
p = tk.StringVar(w, "Прямоугольник")
e = tk.OptionMenu(w, p, "Прямоугольник", "Треугольник")
f = tk.Button(w, text="Счет", command=v)
g = tk.Label(w, text="Итог: -")

a.grid(row=0, column=0, padx=5, pady=5, sticky="e")
b.grid(row=0, column=1, padx=5, pady=5)
c.grid(row=1, column=0, padx=5, pady=5, sticky="e")
d.grid(row=1, column=1, padx=5, pady=5)
e.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")
f.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")
g.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

w.bind("<Return>", lambda q: v())
w.mainloop()