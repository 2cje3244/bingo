import tkinter as tk
import random

class BingoSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("ビンゴ司会システム")

        self.numbers = list(range(1, 76))
        random.shuffle(self.numbers)
        self.selected_numbers = []

        # 見出しを設定
        self.current_number_label = tk.Label(root, text="スタート", font=("Helvetica", 24))
        self.current_number_label.pack(pady=20)

        # ボタンを設定
        self.select_button = tk.Button(root, text="セレクトナンバー", command=self.select_number, font=("Helvetica", 16))
        self.select_button.pack(pady=20)

        # 履歴を設定
        self.history_label = tk.Label(root, text="履歴", font=("Helvetica", 16))
        self.history_label.pack(pady=10)
        self.history_text = tk.Text(root, height=10, width=30, font=("Helvetica", 16))
        self.history_text.pack(pady=10)
        
    def select_number(self):
        if self.numbers:
            
            selected_number = self.numbers.pop(0)
            self.selected_numbers.append(selected_number)

            self.current_number_label.config(text=f"{selected_number}")

            self.history_text.insert(tk.END, f"{selected_number}\n")
            self.history_text.see(tk.END)
            
        else:
            self.current_number_label.config(text="終了！！")

#表示
root = tk.Tk()
app = BingoSystem(root)
root.mainloop()