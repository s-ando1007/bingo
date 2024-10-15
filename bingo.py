import math
import random
import tkinter as tk
from tkinter import messagebox

class bingo:
    def __init__(self, x):
        self.x = x
        self.x.title("ビンゴ")
        self.b = []
        self.a = list(range(1, 76))

        self.y = tk.Label(self.x, text = "次の番号は?", font = ("Arial", 30))
        self.y.pack(pady = 20)

        self.z = tk.Button(self.x, text = "番号を引く", command = self.number, font = ("Arial", 20))
        self.z.pack(pady = 20)

        self.u = tk.Label(self.x, text = "履歴", font = ("Arial", 16))
        self.u.pack(pady = 10)

        self.t = tk.Text(self.x, height = 10, width = 30, font = ("Arial", 16))
        self.t.pack(pady = 10)

    def number(self):
        if self.a:
            p = random.choice(self.a)
            self.a.remove(p)
            self.b.append(p)

            self.y.config(text = f"次の番号: {p}")

            self.t.delete(1.0, tk.END)
            self.t.insert(tk.END, ", ".join(map(str, self.b)))
        else:
            messagebox.showinfo("ゲーム終了", "すべての番号が引かれました")

o = tk.Tk()
q = bingo(o)
o.mainloop()
