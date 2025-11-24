import tkinter as tk
from PIL import Image,ImageTk


def get_xy(x,y,z):
	global wd,ht

	cx,cy=wd/2,ht/2

	f=-550

	x=-(x*f)/(z-f)+cx
	y=(y*f)/(z-f)+cy

	return (x,y)

def draw_floor():
	global area,location,height,ratio




	gnd=-height

	sz=1

	ar=[]

	nx=int(round(area[0]/sz,0))
	nz=int(round(area[1]/sz,0))

	z_=area[1]*location[1]
	for z in range(nz):
		x_=area[0]*-location[0]
		for x in range(nx):

			pa=[[x_,gnd,z_],
				[x_+sz,gnd,z_],
				[x_+sz,gnd,z_-sz],
				[x_,gnd,z_-sz]]

			#print(pa)

			v=clip(pa)

			if v!=None:



				ar.append(v)

			x_+=sz

		z_-=sz

	for i in ar:
		can.create_polygon(i,fill="#323232",outline="#ffffff")

def clip(ar):
	global wd,ht,ratio
	ar_=[]

	for p in ar:


		x,y,z=p
		if z<0:
			return None
		x_,y_=get_xy(x*ratio,y*ratio,z*ratio)

		


		ar_.append(((round(x_,0),round(y_,0))))




	return ar_



root=tk.Tk()
wd,ht=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry(f"{wd}x{ht}+0+0")


area=(50,50)#meters
location=(0.5,1)
height=1.7018
ratio=(ht/2)/height



can=tk.Canvas(width=wd,height=ht,bg="#000000",relief="flat",highlightthickness=0,border=0)
can.place(in_=root,x=0,y=0)

draw_floor()

root.mainloop()

