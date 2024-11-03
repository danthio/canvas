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
	global area,myloc,myloc_
	global x_ang,y_ang


	can.delete("all")

	draw_floor()


	xa,ya=get_xy(0,0,3)
	xb,yb=get_xy(0,1.7,3)

	#can.create_line(xa,ya, xb,yb, fill="cyan")

	can.create_oval(wd/2-3,ht/2-3, wd/2+3,ht/2+3,outline="#ffffff")





	l1=[0.25,0.25]

	xx=-area[0]*myloc[0]+area[0]*l1[0]
	zz=area[1]*myloc[1]-area[1]*l1[1]+myloc_[-1]


	x1,y1,z1=rot(xx,0,zz,myloc_,x_ang,y_ang)
	x2,y2,z2=rot(xx,1.7,zz,myloc_,x_ang,y_ang)


	xx1,yy1=get_xy(x1,y1,z1)
	xx2,yy2=get_xy(x2,y2,z2)

	st=0

	if z1<0 or z2<0:
		st=1

	if st==0:

		can.create_line(xx1,yy1, xx2,yy2,fill="cyan")










	l1=[0.4,0.4]

	xx=-area[0]*myloc[0]+area[0]*l1[0]
	zz=area[1]*myloc[1]-area[1]*l1[1]+myloc_[-1]

	x1,y1,z1=rot(xx,0,zz,myloc_,x_ang,y_ang)
	x2,y2,z2=rot(xx,1.7,zz,myloc_,x_ang,y_ang)
	x3,y3,z3=rot(xx,1.7,zz+0.5,myloc_,x_ang,y_ang)

	x4,y4,z4=rot(xx,1.7,zz+0.5,[xx,1.7,zz],0,45)
	x4,y4,z4=rot(x4,y4,z4,[xx,1.7,zz],90,0)
	x4,y4,z4=rot(x4,y4,z4,myloc_,x_ang,y_ang)












	








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



	draw_person([0.7,0.3],1.7,-45, 0,0,0, 90,50,20, 0,0,0, 45,50,20, 0,0, 45,-90, 0,0, 45,-20 )









def draw_person(l,ht,face_ang, la1x,la2x,la3x, la1y,la2y,la3y, ra1x,ra2x,ra3x, ra1y,ra2y,ra3y, ll1x,ll2x, ll1y,ll2y, rl1x,rl2x, rl1y,rl2y):

	global x_ang,y_ang
	global myloc,myloc_,area

	r=ht/1.881


	xx=-area[0]*myloc[0]+area[0]*l[0]
	zz=area[1]*myloc[1]-area[1]*l[1]+myloc_[-1]	


	p1=[xx,0+ht,zz]
	p2=[xx,0+ht-0.389*r,zz]


	#left arm
	p3=[xx-0.2*r,0+ht-0.389*r,zz]	
	p4=[xx-0.2*r,0+ht-(0.389+0.302)*r,zz]
	p5=[xx-0.2*r,0+ht-(0.389+0.302+0.269)*r,zz]
	p6=[xx-0.2*r,0+ht-(0.389+0.302+0.269+0.211)*r,zz]



	p4=rot(*p4,p3,0,la1y)
	p4=rot(*p4,p3,la1x,0)
	p5=rot(*p5,p3,0,la1y)
	p5=rot(*p5,p3,la1x,0)
	p6=rot(*p6,p3,0,la1y)
	p6=rot(*p6,p3,la1x,0)

	p5=rot(*p5,p4,0,la2y)
	p5=rot(*p5,p4,la2x,0)
	p6=rot(*p6,p4,0,la2y)
	p6=rot(*p6,p4,la2x,0)

	p6=rot(*p6,p5,0,la3y)
	p6=rot(*p6,p5,la3x,0)

	#right arm
	p7=[xx+0.2*r,0+ht-0.389*r,zz]	
	p8=[xx+0.2*r,0+ht-(0.389+0.302)*r,zz]
	p9=[xx+0.2*r,0+ht-(0.389+0.302+0.269)*r,zz]
	p10=[xx+0.2*r,0+ht-(0.389+0.302+0.269+0.211)*r,zz]

	p8=rot(*p8,p7,0,ra1y)
	p8=rot(*p8,p7,ra1x,0)

	p9=rot(*p9,p7,0,ra1y)
	p9=rot(*p9,p7,ra1x,0)

	p10=rot(*p10,p7,0,ra1y)
	p10=rot(*p10,p7,ra1x,0)

	p9=rot(*p9,p8,0,ra2y)
	p9=rot(*p9,p8,ra2x,0)
	p10=rot(*p10,p8,0,ra2y)
	p10=rot(*p10,p8,ra2x,0)

	p10=rot(*p10,p9,0,ra3y)
	p10=rot(*p10,p9,ra3x,0)


	#left leg

	p11=[xx-0.14*r,0+ht-(0.389+0.488)*r,zz]
	p12=[xx-0.14*r,0+ht-(0.389+0.488+0.46)*r,zz]
	p13=[xx-0.14*r,0+ht-(0.389+0.488+0.46+0.45)*r,zz]	
	p14=[xx-0.14*r,0+ht-(0.389+0.488+0.46+0.45+0.094)*r,zz]	

	ll1x,ll2x, ll1y,ll2y

	p12=rot(*p12,p11,0,ll1y)
	p12=rot(*p12,p11,ll1x,0)
	p13=rot(*p13,p11,0,ll1y)
	p13=rot(*p13,p11,ll1x,0)
	p14=rot(*p14,p11,0,ll1y)
	p14=rot(*p14,p11,ll1x,0)

	p13=rot(*p13,p12,0,ll2y)
	p13=rot(*p13,p12,ll2x,0)

	p14=rot(*p14,p12,0,ll2y)
	p14=rot(*p14,p12,ll2x,0)	

	#rigth leg
	p15=[xx+0.14*r,0+ht-(0.389+0.488)*r,zz]
	p16=[xx+0.14*r,0+ht-(0.389+0.488+0.46)*r,zz]
	p17=[xx+0.14*r,0+ht-(0.389+0.488+0.46+0.45)*r,zz]	
	p18=[xx+0.14*r,0+ht-(0.389+0.488+0.46+0.45+0.094)*r,zz]



	p16=rot(*p16,p15,0,rl1y)
	p16=rot(*p16,p15,rl1x,0)
	p17=rot(*p17,p15,0,rl1y)
	p17=rot(*p17,p15,ll1x,0)
	p18=rot(*p18,p15,0,rl1y)
	p18=rot(*p18,p15,rl1x,0)

	p17=rot(*p17,p16,0,rl2y)
	p17=rot(*p17,p16,rl2x,0)
	p18=rot(*p18,p16,0,rl2y)
	p18=rot(*p18,p16,rl2x,0)	








	p19=[xx,0+ht-(0.389+0.488)*r,zz]


	p1=rot(*p1,[xx,0,zz],face_ang,0)
	p1=rot(*p1,myloc_,x_ang,y_ang)

	p2=rot(*p2,[xx,0,zz],face_ang,0)
	p2=rot(*p2,myloc_,x_ang,y_ang)

	p3=rot(*p3,[xx,0,zz],face_ang,0)
	p3=rot(*p3,myloc_,x_ang,y_ang)

	p4=rot(*p4,[xx,0,zz],face_ang,0)
	p4=rot(*p4,myloc_,x_ang,y_ang)

	p5=rot(*p5,[xx,0,zz],face_ang,0)
	p5=rot(*p5,myloc_,x_ang,y_ang)

	p6=rot(*p6,[xx,0,zz],face_ang,0)
	p6=rot(*p6,myloc_,x_ang,y_ang)

	p7=rot(*p7,[xx,0,zz],face_ang,0)
	p7=rot(*p7,myloc_,x_ang,y_ang)

	p8=rot(*p8,[xx,0,zz],face_ang,0)
	p8=rot(*p8,myloc_,x_ang,y_ang)

	p9=rot(*p9,[xx,0,zz],face_ang,0)
	p9=rot(*p9,myloc_,x_ang,y_ang)

	p10=rot(*p10,[xx,0,zz],face_ang,0)
	p10=rot(*p10,myloc_,x_ang,y_ang)

	p11=rot(*p11,[xx,0,zz],face_ang,0)
	p11=rot(*p11,myloc_,x_ang,y_ang)

	p12=rot(*p12,[xx,0,zz],face_ang,0)
	p12=rot(*p12,myloc_,x_ang,y_ang)

	p13=rot(*p13,[xx,0,zz],face_ang,0)
	p13=rot(*p13,myloc_,x_ang,y_ang)

	p14=rot(*p14,[xx,0,zz],face_ang,0)
	p14=rot(*p14,myloc_,x_ang,y_ang)

	p15=rot(*p15,[xx,0,zz],face_ang,0)
	p15=rot(*p15,myloc_,x_ang,y_ang)

	p16=rot(*p16,[xx,0,zz],face_ang,0)
	p16=rot(*p16,myloc_,x_ang,y_ang)

	p17=rot(*p17,[xx,0,zz],face_ang,0)
	p17=rot(*p17,myloc_,x_ang,y_ang)

	p18=rot(*p18,[xx,0,zz],face_ang,0)
	p18=rot(*p18,myloc_,x_ang,y_ang)

	p19=rot(*p19,[xx,0,zz],face_ang,0)
	p19=rot(*p19,myloc_,x_ang,y_ang)



	can.create_line(get_xy(*p1),get_xy(*p2),get_xy(*p19),fill="red")

	can.create_line(get_xy(*p2),get_xy(*p3),get_xy(*p4),get_xy(*p5),get_xy(*p6),fill="red")
	can.create_line(get_xy(*p2),get_xy(*p7),get_xy(*p8),get_xy(*p9),get_xy(*p10),fill="red")

	can.create_line(get_xy(*p19),get_xy(*p11),get_xy(*p12),get_xy(*p13),get_xy(*p14),fill="red")
	can.create_line(get_xy(*p19),get_xy(*p15),get_xy(*p16),get_xy(*p17),get_xy(*p18),fill="red")



def draw_floor():
	global gnd,area,myloc,myloc_
	global x_ang,y_ang


	tile_x,tile_y=1,1   #in meters

	


	n_xtile=area[0]/tile_x
	n_ytile=area[1]/tile_y





	yv=area[1]*myloc[1]+myloc_[-1]

	zst=0

	for y in range(int(n_ytile)):

		xv=-area[0]*myloc[0]


		for x in range(int(n_xtile)):
			ar=[]
			a=[[0,0],[1,0],[1,1],[0,1]]

			zst=0

			


			for x_ in a:

				xx,yy,zz=rot(xv+x_[0]*tile_x,0,yv-x_[1]*tile_y,myloc_,x_ang,y_ang)

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





def draw_wall():


	global gnd,area,myloc,myloc_
	global x_ang,y_ang


	tile_x,tile_y=1,1   #in meters

	


	n_xtile=area[0]/tile_x
	n_ytile=5/tile

	




def rot(x,y,z,ref,ax,ay,az=0):



	# Define the point to be rotated and the rotation center
	point = np.array([x,y,z])
	center = np.array(ref)

	# Rotation angles
	theta_z = np.radians(ay)  # Rotate 90 degrees around Z-axis
	theta_y = np.radians(-ax)  # Rotate 20 degrees around Y-axis
	theta_x = np.radians(az) 

	# Define the Z-axis rotation matrix
	rotation_matrix_z = np.array([
	    [np.cos(theta_x), -np.sin(theta_x), 0],
	    [np.sin(theta_x), np.cos(theta_x), 0],
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
	rotated_point_y = np.dot(rotation_matrix_x, rotated_point_z)

	#rotated_point_xyz = np.dot(rotation_matrix_z, rotated_point_y)

	# Step 4: Translate back to the original center
	final_rotated_point = rotated_point_y + center

	return final_rotated_point




def check_keys():

	global x_ang, y_ang,area,myloc



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
		if not y_ang-5<-90:
			y_ang-=15
			main()


	if keyboard.is_pressed('down'):
		if not y_ang+5>30:
			y_ang+=15
			main()



	if keyboard.is_pressed('w') or keyboard.is_pressed('W'):


		if keyboard.is_pressed("d") or keyboard.is_pressed("D"):
			x_ang+=15


		elif keyboard.is_pressed("a") or keyboard.is_pressed("A"):
			x_ang-=15


		v=0.6/area[0]

		x=v*math.sin(math.radians(180+x_ang))
		y=v*math.cos(math.radians(180+x_ang))

		myloc[0]-=x
		myloc[1]+=y



		main()


	elif keyboard.is_pressed('s') or keyboard.is_pressed('S'):


		if keyboard.is_pressed("d") or keyboard.is_pressed("D"):
			x_ang+=15


		elif keyboard.is_pressed("a") or keyboard.is_pressed("A"):
			x_ang-=15



		v=0.6/area[0]

		x=v*math.sin(math.radians(180+x_ang+180))
		y=v*math.cos(math.radians(180+x_ang+180))

		myloc[0]-=x
		myloc[1]+=y




		main()

	elif keyboard.is_pressed("d") or keyboard.is_pressed("D"):

		v=0.6/area[0]

		x=v*math.sin(math.radians(180+x_ang+180-90))
		y=v*math.cos(math.radians(180+x_ang+180-90))

		myloc[0]-=x
		myloc[1]+=y



		main()


	elif keyboard.is_pressed("a") or keyboard.is_pressed("A"):

		v=0.6/area[0]

		x=v*math.sin(math.radians(180+x_ang+180+90))
		y=v*math.cos(math.radians(180+x_ang+180+90))

		myloc[0]-=x
		myloc[1]+=y



		main()

	root.after(10,check_keys)	


root=tk.Tk()
wd=int(root.winfo_screenwidth())
ht=int(root.winfo_screenheight())

root.wm_attributes("-fullscreen",1)




gnd=-ht/2
hvar=-gnd/2
area=[20,20]#in meters

myloc=[0.5,0.5]
myloc_=[0,0,3]

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