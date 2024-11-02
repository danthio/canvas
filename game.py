import tkinter as tk
import math
import keyboard
import pyautogui
import time
import numpy as np


def get_xy(xx,yy,zz):

	global wd,ht,gnd,hvar

	xx=xx*hvar
	yy=gnd+yy*hvar
	zz=zz*hvar


	cx,cy=wd/2,ht/2
	f=-550

	xx*=wd
	yy*=wd
	zz*=wd

	xx=-xx


	x=((xx*f)/(zz-f))+cx
	y=((yy*f)/(zz-f))+cy


	return x,y



def main():
	global can,ht,wd
	global area,loc,loc2
	global x_ang,y_ang


	can.delete("all")

	draw_floor()


	xa,ya=get_xy(0,0,3)
	xb,yb=get_xy(0,1.7,3)

	can.create_line(xa,ya, xb,yb, fill="cyan")

	can.create_oval(wd/2-3,ht/2-3, wd/2+3,ht/2+3,outline="#ffffff")





	l1=[0.25,0.25]

	xx=-area[0]*loc[0]+area[0]*l1[0]
	zz=area[1]*loc[1]-area[1]*l1[1]+loc2[-1]


	x1,y1,z1=rot(xx,0,zz,loc2,x_ang,y_ang)
	x2,y2,z2=rot(xx,1.7,zz,loc2,x_ang,y_ang)


	xx1,yy1=get_xy(x1,y1,z1)
	xx2,yy2=get_xy(x2,y2,z2)

	st=0

	if z1<0 or z2<0:
		st=1

	if st==0:

		can.create_line(xx1,yy1, xx2,yy2,fill="cyan")










	l1=[0.4,0.4]

	xx=-area[0]*loc[0]+area[0]*l1[0]
	zz=area[1]*loc[1]-area[1]*l1[1]+loc2[-1]

	x1,y1,z1=rot(xx,0,zz,loc2,x_ang,y_ang)
	x2,y2,z2=rot(xx,1.7,zz,loc2,x_ang,y_ang)
	x3,y3,z3=rot(xx,1.7,zz+0.5,loc2,x_ang,y_ang)

	x4,y4,z4=rot(xx,1.7,zz+0.5,[xx,1.7,zz],0,10)	
	x4,y4,z4=rot(x4,y4,z4,loc2,x_ang,y_ang)






	








	xx1,yy1=get_xy(x1,y1,z1)
	xx2,yy2=get_xy(x2,y2,z2)
	xx3,yy3=get_xy(x3,y3,z3)
	xx4,yy4=get_xy(x4,y4,z4)

	st=0

	if z1<0 or z2<0:
		st=1

	if st==0:

		can.create_line(xx1,yy1, xx2,yy2, xx3,yy3,fill="red")

		can.create_line(xx2,yy2, xx4,yy4, fill="yellow")









def draw_person(ht):
	pass

def draw_floor():
	global gnd,area,loc,loc2
	global x_ang,y_ang


	tile_x,tile_y=1,1   #in meters

	


	n_xtile=area[0]/tile_x
	n_ytile=area[1]/tile_y





	yv=area[1]*loc[1]+loc2[-1]

	zst=0

	for y in range(int(n_ytile)):

		xv=-area[0]*loc[0]


		for x in range(int(n_xtile)):
			ar=[]
			a=[[0,0],[1,0],[1,1],[0,1]]

			zst=0

			


			for x_ in a:

				xx,yy,zz=rot(xv+x_[0]*tile_x,0,yv-x_[1]*tile_y,loc2,x_ang,y_ang)

				#print(xv+x_[0]*tile_x,0,yv-x_[1]*tile_y)

				_x,_y=get_xy(xx,yy,zz)

				if zz<0:
					zst=1

				ar.append(_x)
				ar.append(_y)

			#print(ar)


			c=0
			c2=0
			c3=0
			c_=1
			for _ in range(len(ar)):

				if ar[_]<0:
					c+=1

				if c_%2==0:
					if ar[_]<0:
						c2+=1

				else:
					if ar[_]<0:
						c3+=1


				c_+=1


			
			if not c2==4:


				if zst==0:


					can.create_polygon(ar,fill="#222222",outline="#666666")

			xv+=tile_x


		#if yv<0:
		#	break#
		yv-=tile_y











def rot(x,y,z,ref,ax,ay):



	# Define the point to be rotated and the rotation center
	point = np.array([x,y,z])
	center = np.array(ref)

	# Rotation angles
	theta_z = np.radians(ay)  # Rotate 90 degrees around Z-axis
	theta_y = np.radians(-ax)  # Rotate 20 degrees around Y-axis

	# Define the Z-axis rotation matrix
	rotation_matrix_z = np.array([
	    [np.cos(theta_z), -np.sin(theta_z), 0],
	    [np.sin(theta_z), np.cos(theta_z), 0],
	    [0, 0, 1]
	])

	# Define the Y-axis rotation matrix
	rotation_matrix_y = np.array([
	    [np.cos(theta_y), 0, np.sin(theta_y)],
	    [0, 1, 0],
	    [-np.sin(theta_y), 0, np.cos(theta_y)]
	])


	rotation_matrix_x = np.array([
	    [1, 0, 0],
	    [0, np.cos(theta_z), -np.sin(theta_z)],
	    [0, np.sin(theta_z), np.cos(theta_z)]
	])


	# Step 1: Translate the point so the rotation center is at the origin
	translated_point = point - center

	# Step 2: Apply the Z-axis rotation
	rotated_point_z = np.dot(rotation_matrix_y, translated_point)

	# Step 3: Apply the Y-axis rotation
	rotated_point_yz = np.dot(rotation_matrix_x, rotated_point_z)

	# Step 4: Translate back to the original center
	final_rotated_point = rotated_point_yz + center

	return final_rotated_point




def check_keys():

	global x_ang, y_ang,area,loc



	currentMouseX, currentMouseY = pyautogui.position()

	"""
	if currentMouseX>motionx:
		x_ang+=	15
		pyautogui.moveTo(wd/2, ht/2)
		main()
	elif currentMouseX<motionx:
		x_ang-=15
		pyautogui.moveTo(wd/2, ht/2)

		main()
	"""

	

	if keyboard.is_pressed('left'):
		x_ang-=15
		main()
	if keyboard.is_pressed('right'):
		x_ang+=15
		main()
	if keyboard.is_pressed('up'):

		if not y_ang+5>30:
			y_ang+=15
			main()

	if keyboard.is_pressed('down'):
		if not y_ang-5<-90:
			y_ang-=15
			main()



	if keyboard.is_pressed('w') or keyboard.is_pressed('W'):


		if keyboard.is_pressed("d") or keyboard.is_pressed("D"):
			x_ang+=15


		elif keyboard.is_pressed("a") or keyboard.is_pressed("A"):
			x_ang-=15


		v=0.6/area[0]

		x=v*math.sin(math.radians(180+x_ang))
		y=v*math.cos(math.radians(180+x_ang))

		loc[0]-=x
		loc[1]+=y



		main()


	elif keyboard.is_pressed('s') or keyboard.is_pressed('S'):


		if keyboard.is_pressed("d") or keyboard.is_pressed("D"):
			x_ang+=15


		elif keyboard.is_pressed("a") or keyboard.is_pressed("A"):
			x_ang-=15



		v=0.6/area[0]

		x=v*math.sin(math.radians(180+x_ang+180))
		y=v*math.cos(math.radians(180+x_ang+180))

		loc[0]-=x
		loc[1]+=y




		main()

	elif keyboard.is_pressed("d") or keyboard.is_pressed("D"):

		v=0.6/area[0]

		x=v*math.sin(math.radians(180+x_ang+180-90))
		y=v*math.cos(math.radians(180+x_ang+180-90))

		loc[0]-=x
		loc[1]+=y



		main()


	elif keyboard.is_pressed("a") or keyboard.is_pressed("A"):

		v=0.6/area[0]

		x=v*math.sin(math.radians(180+x_ang+180+90))
		y=v*math.cos(math.radians(180+x_ang+180+90))

		loc[0]-=x
		loc[1]+=y



		main()

	root.after(10,check_keys)	


root=tk.Tk()
wd=int(root.winfo_screenwidth())
ht=int(root.winfo_screenheight())

root.wm_attributes("-fullscreen",1)




gnd=-ht/2
hvar=-gnd/2
area=[20,20]#in meters

loc=[0.5,0.5]
loc2=[0,0,3]

x_ang=0
y_ang=0

def mouse_motion():
	global motionx,motiony,x_ang,y_ang


	currentMouseX, currentMouseY = pyautogui.position()


	if currentMouseX>motionx:
		x_ang+=15
		pyautogui.moveTo(wd/2, ht/2)
		main()
	elif currentMouseX<motionx:
		x_ang-=15
		pyautogui.moveTo(wd/2, ht/2)

		main()



	


	root.after(10,mouse_motion)


motionx,motiony=wd/2,ht/2
can=tk.Canvas(width=wd,height=ht,relief="flat",highlightthickness=0,border=0,bg="skyblue",cursor="none")
can.place(in_=root,x=0,y=0)



main()

check_keys()
#mouse_motion()
root.mainloop()