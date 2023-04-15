# 主視窗建立 2 個視窗區塊，第 1 個視窗區塊包含 1 個標籤及 1 個文字編輯元件。
# 第 2 個視窗區塊包含 2 個按鈕元件。

import tkinter as tk
win = tk.Tk()

frame1 = tk.Frame(win)
frame1.pack()
label1 = tk.Label(frame1, text = "標籤一:")
entry1 = tk.Entry(frame1)
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)

frame2 = tk.Frame(win)
frame2.pack()
button1 = tk.Button(frame2, text="確定")
button2 = tk.Button(frame2, text="取消")
button1.grid(row = 0, column = 0)
button2.grid(row = 0, column = 1)
win.mainloop()