import tkinter as tk
from tkinter import messagebox

def check_even_gui():
    try:
        
        val = entry.get().strip()
        if not val:
            return
            
        num = int(val)
        
        if num % 2 == 0:
            result_label.config(text=f"{num}: 짝수입니다! ✅", fg="#2ecc71")
        else:
            result_label.config(text=f"{num}: 홀수입니다! ⭕", fg="#e67e22")
            
    except ValueError:
        messagebox.showerror("입력 오류", "정수만 입력해주세요!")
        entry.delete(0, tk.END)

# 메인
root = tk.Tk()
root.title("홀짝 판별기 v1.1")
root.geometry("350x250")
root.configure(bg="white") 

# 제목 
title_label = tk.Label(root, text="숫자를 입력하세요", 
                       font=("Arial", 14, "bold"), bg="white", fg="black", pady=20)
title_label.pack()

entry = tk.Entry(root, font=("Arial", 14), justify='center', 
                 bg="#eeeeee", fg="black", insertbackground="black", highlightthickness=1)
entry.pack(pady=5)
entry.focus_set()

# 버튼
check_button = tk.Button(root, text="판별하기", command=check_even_gui,
                         width=15, bg="#3498db", fg="black", 
                         font=("Arial", 10, "bold"))
check_button.pack(pady=15)

# 결과 
result_label = tk.Label(root, text="결과가 여기 표시됩니다.", 
                        font=("Arial", 11), bg="white", fg="gray")
result_label.pack()

root.mainloop()