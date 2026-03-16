import tkinter as tk
from tkinter import messagebox

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

def start_calc():
    try:
        
        val = entry.get()
        n = int(val)
        
        
        res = fact(n)
        
        
        res_label.config(text=f"결과: {res}", fg="black")
    except:
        messagebox.showerror("오류", "정수 넣어야함")

# gui
win = tk.Tk()
win.title("팩토리얼 계산기")
win.geometry("300x250")
win.configure(bg="white")

# 멘트
tk.Label(win, text="팩토리얼 구할 숫자:", bg="white", fg="black").pack(pady=10)


entry = tk.Entry(win, bg="#eeeeee", fg="black", insertbackground="black")
entry.pack(pady=5)

# 버튼
btn = tk.Button(win, text="계산 시작", command=start_calc)
btn.pack(pady=10)

res_label = tk.Label(win, text="결과 표시", bg="white", fg="gray")
res_label.pack(pady=20)

win.mainloop()