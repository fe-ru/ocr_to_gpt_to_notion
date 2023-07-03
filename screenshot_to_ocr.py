import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

def move_screenshots():
    # デスクトップのパスを指定
    desktop_path = "/Users/bocmitsuhashi/Desktop" 

    # 現在の時間を取得し、フォルダ名に使えるように文字列に変換
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    
    # "インスタ"フォルダ内に作成するフォルダ名
    folder_name = f"{desktop_path}/インスタ/Screenshots_{timestamp}"

    # "Screenshots" フォルダがない場合は作成
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # デスクトップ上のすべてのファイルをチェック
    for file_name in os.listdir(desktop_path):
        # ファイル名が "Screenshot" で始まるかどうかを確認
        if file_name.startswith("スクリーンショット"):
            # そのファイルを "Screenshots" フォルダに移動
            shutil.move(desktop_path + "/" + file_name, folder_name + "/" + file_name)
    messagebox.showinfo('Information', 'Screenshots have been moved')

root = tk.Tk()
button = tk.Button(root, text="Move Screenshots", command=move_screenshots)
button.pack()

root.mainloop()
