import tkinter as tk
from tkinter import messagebox

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False  
    return True

def find_primes():
    try:
        limit = int(entry.get())
        prime_list = []

        for i in range(1, limit + 1):
            if is_prime(i):
                prime_list.append(i)
        
        # 결과창 지우고 새로 쓰기
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, str(prime_list))
        
    except:
        messagebox.showerror("에러", "숫자만 써야함")

root = tk.Tk()
root.title("소수 찾기 프로그램")
root.geometry("400x400")
root.configure(bg="white")


tk.Label(root, text="범위 입력:", bg="white", fg="black").pack(pady=10)

entry = tk.Entry(root, bg="#eeeeee", fg="black", insertbackground="black")
entry.pack()

btn = tk.Button(root, text="소수 찾기 시작", command=find_primes)
btn.pack(pady=10)

tk.Label(root, text="결과창:", bg="white", fg="black").pack()

#결과
result_text = tk.Text(root, height=10, width=40, bg="#f8f8f8", fg="black")
result_text.pack(pady=10)

root.mainloop()