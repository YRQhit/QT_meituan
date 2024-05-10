import tkinter as tk

def on_submit():
    user_input = entry.get()
    print("You entered:", user_input)

# 创建主窗口
root = tk.Tk()
root.title("输入框示例")

# 创建输入框
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# 创建提交按钮
submit_btn = tk.Button(root, text="提交", command=on_submit)
submit_btn.pack()

# 运行主循环
root.mainloop()
