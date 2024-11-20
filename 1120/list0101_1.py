import tkinter  # tkinterモジュールをインポートする

root = tkinter.Tk() # メインウィンドウを作成する
root.geometry("400x200") # ウィンドウのサイズを設定する
root.title("PythonでGUIを扱う") # ウィンドウのタイトルを設定する

label = tkinter.Label(root, text="ゲーム開発の一歩", font=("Times New Roman", 20)) # ラベルを作成する
label.place(x=80, y=60) # ラベルを配置する

root.mainloop() # メインループがなければウィンドウは一瞬表示されて消える
