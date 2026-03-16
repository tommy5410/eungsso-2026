import tkinter as tk
from tkinter import messagebox

def fahrenheit_to_celsius(f_temp):
    return (f_temp - 32) * 5 / 9

def cm_to_inch(cm):
    return cm / 2.54

# gui
def handle_temp_convert():
    try:
        f_val = float(entry_temp.get())
        c_val = fahrenheit_to_celsius(f_val)
        label_temp_result.config(text=f"결과: {c_val:.2f} °C", fg="#2c3e50")
    except ValueError:
        messagebox.showerror("입력 오류", "온도에 숫자를 입력해주세요.")

def handle_length_convert():
    try:
        cm_val = float(entry_length.get())
        inch_val = cm_to_inch(cm_val)
        label_length_result.config(text=f"결과: {inch_val:.2f} inch", fg="#2c3e50")
    except ValueError:
        messagebox.showerror("입력 오류", "길이에 숫자를 입력해주세요.")

root = tk.Tk()
root.title("단위 변환기 v1.0")
root.geometry("400x350")
root.configure(bg="#ffffff") 

#온도
tk.Label(root, text="[ 온도 변환: F → C ]", font=("Arial", 12, "bold"), 
         bg="#ffffff", fg="#34495e").pack(pady=(20, 5))

entry_temp = tk.Entry(root, font=("Arial", 12), justify='center',
                      bg="#f8f9fa", fg="black", insertbackground="black")
entry_temp.pack()

tk.Button(root, text="온도 변환", command=handle_temp_convert, 
          bg="#3498db", fg="black").pack(pady=5)

label_temp_result = tk.Label(root, text="결과 표시.", bg="#ffffff", fg="gray")
label_temp_result.pack()


tk.Label(root, text="", bg="#ffffff").pack(pady=10)

# 길이
tk.Label(root, text="[ 길이 변환: cm → inch ]", font=("Arial", 12, "bold"), 
         bg="#ffffff", fg="#34495e").pack(pady=5)

entry_length = tk.Entry(root, font=("Arial", 12), justify='center',
                        bg="#f8f9fa", fg="black", insertbackground="black")
entry_length.pack()

tk.Button(root, text="길이 변환", command=handle_length_convert, 
          bg="#e67e22", fg="black").pack(pady=5)

label_length_result = tk.Label(root, text="결과 표시.", bg="#ffffff", fg="gray")
label_length_result.pack()

root.mainloop()