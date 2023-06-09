# 密碼確認視窗
# 使用者可在文字編輯元件中輸入密碼，若輸入「1234」表示密碼正確，顯示歡迎登入訊息；
# 若輸入的密碼錯誤，顯示修改密碼訊息。

def checkPW():
    if (pw.get() == "1234"):
        msg.set("密碼正確，歡迎登入!")
    else:
        msg.set("密碼錯誤，請修正密碼!")

import tkinter as tk

win = tk.Tk()
pw = tk.StringVar()
msg = tk.StringVar()
label = tk.Label(win, text="請輸入密碼:")
label.pack()
entry = tk.Entry(win, textvariable=pw)
entry.pack()
button = tk.Button(win, text="登入", command=checkPW)
button.pack()
lblmsg = tk.Label(win, fg="red", textvariable=msg)
lblmsg.pack()
win.mainloop()