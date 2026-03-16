import tkinter as tk

def calculate_sums():
    
    even_sum = sum([x for x in range(1, 101) if x % 2 == 0])
    
    label_res.config(text=f"합계: {even_sum}", fg="black")

root = tk.Tk()
root.title("짝수 합 계산기")
root.geometry("300x200")
root.configure(bg="white")


tk.Label(root, text="1-100까지 짝수 합 구하기", bg="white", fg="black", 
         font=("Arial", 12, "bold")).pack(pady=20)

# 버튼
btn = tk.Button(root, text="합계 보기", command=calculate_sums)
btn.pack(pady=10)

# 결과
label_res = tk.Label(root, text="결과 표시", bg="white", fg="gray")
label_res.pack(pady=10)

root.mainloop()