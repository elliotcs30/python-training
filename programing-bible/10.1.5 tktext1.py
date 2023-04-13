# 元件參數設定

import tkinter as tk

win = tk.Tk()

text = tk.Text(win)
text.insert(tk.INSERT, "Tkinter 模組是圖形使用者介面，\n")
text.insert(tk.INSERT, "雖然功能略為陽春，\n")
text.insert(tk.INSERT, "但已足夠一般應用程式使用，\n")
text.insert(tk.INSERT, "而且是內含於 Python 系統中，\n")
text.insert(tk.END, "不需另外安裝即可使用。")

text.pack()
text.config(state=tk.DISABLED)
win.mainloop()