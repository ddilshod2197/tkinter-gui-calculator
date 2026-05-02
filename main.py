import tkinter as tk

class Kalkulyator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Kalkulyator")
        self.entry = tk.Entry(self.root, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4)
        self.kiritish()
        self.root.mainloop()

    def kiritish(self):
        butunlar = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        row_val = 1
        col_val = 0
        for butun in butunlar:
            tk.Button(self.root, text=butun, width=10, command=lambda butun=butun: self.click(butun)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        tk.Button(self.root, text="C", width=21, command=self.clear).grid(row=row_val, column=0, columnspan=2)
        tk.Button(self.root, text="Del", width=21, command=self.delete).grid(row=row_val, column=2, columnspan=2)

    def click(self, butun):
        if butun == '=':
            try:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(eval(self.entry.get())))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Xatolik")
        else:
            self.entry.insert(tk.END, butun)

    def clear(self):
        self.entry.delete(0, tk.END)

    def delete(self):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current[:-1])

Kalkulyator()
