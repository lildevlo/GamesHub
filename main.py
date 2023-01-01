from tkinter import *

root = Tk()
root.title("Game Launcher")
root.geometry('900x600')
root.iconbitmap("images/icon.ico")

bg = PhotoImage(file="images/bg.png")
canvas1 = Canvas(root, width=400, height=400)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg, anchor="nw")

root.mainloop()
