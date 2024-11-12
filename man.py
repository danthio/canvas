import tkinter as tk
from PIL import Image,ImageTk


def b1(e):

	print(e.x,e.y)



root=tk.Tk()
root.geometry("438x486+0+0")


can=tk.Canvas(width=438,height=486)
can.place(in_=root,x=0,y=0)

can.bind("<Button-1>",b1)


im=ImageTk.PhotoImage(file="man.png")

can.create_image(0,0,image=im,anchor="nw")





root.mainloop()

