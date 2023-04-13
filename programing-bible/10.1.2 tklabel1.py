# pack 方式是將元件視為矩形物件顯示。

import tkinter as tk

win = tk.Tk()

label1 = tk.Label(win, text = "這是標籤元件!", fg = "red", bg = "yellow", font = ("新細明體", 12), pady = 10)
label1.pack()
win.mainloop()