import tkinter
import os
print("Current Working Directory:", os.getcwd())
root = tkinter.Tk()
root.title("Canvasに画像を描画する")

canvas = tkinter.Canvas(width=480, height=300)
canvas.pack() # pack()を呼び出さないと、canvasは作成されていても画面に表示されない

img_bg = tkinter.PhotoImage(file="Chapter1/park.png")
canvas.create_image(240, 150, image=img_bg)

root.mainloop()
