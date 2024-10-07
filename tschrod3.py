from math import *
from tkinter import *
import cmath
import keyboard

root=Tk()
root.title("1-D time dependent Schrodinger eq")
root.geometry("1920x1080")
graph=Canvas(root,width=300,height=200,bg="black")
graph.pack(fill="both",expand=True)


y,yn,yr,yi=[],[],[],[]
x=[]
p=[]
V=[]
n=100
for i in range(n+1):
    x.append(i)
    y.append(0)
    p.append(y[i]**2)
    V.append(.001*(x[i]-50)**2)
    yn.append(y[i])
    yr.append(y[i])
    yi.append(y[i])


def convert(coords,obs,theta):
    x,y,z=coords[0],coords[1],coords[2]
    
    x,z,y=x,y,z
    obsx,obsy,obsz=obs[0],obs[1],obs[2]

    xr=x-obsx
    yr=y-obsy
    zr=z-obsz
    
    dyz=((yr)**2+(zr)**2)**.5
    dxz=((xr)**2+(zr)**2)**.5

    xp,yp=500,500
    
    if dyz>0:
        xp=1920*(xr/(2*dyz)*tan(theta)+.5) #magic
    if dxz>0: 
        yp=1080*(yr/(2*dxz)*tan(theta)+.5)

    #if abs(xp)>1920 or abs(yp)>1080:
        #xp,yp=0,0
        
    a=[xp,yp]
    return a

cont=1
obs=[50,30,-140]
theta=120*pi/180
speed=.5
global phi
phi=0
anglespeed=.01

ds=1 #space distance
dt=.004 #time distance


while cont==1:
    
    for i in range(1,len(x)-1):
        lap=(y[i+1]+y[i-1]-2*y[i])/(2*ds) #laplacian
        yn[i]+=(-lap+V[i])/cmath.sqrt(-1)*dt #integrate

    for i in range(1,len(x)-1): 
        y[i]=yn[i]#copy values to iterate properly
        p[i]=.1*abs(y[i])**2
        yr[i]=y[i].real
        yi[i]=y[i].imag

    for i in range(10): #draw axes
        xp,yp=convert([i*n/10,0,0],obs,theta)
        xp2,yp2=convert([i*n/10,n,0],obs,theta)
        graph.create_line(xp,yp,xp2,yp2,fill="green",width=2)
        #xp,yp=convert([i*n/10,0,0],obs,theta)
        #xp2,yp2=convert([i*n/10,-n,0],obs,theta)
        #graph.create_line(xp,yp,xp2,yp2,fill="green",width=2)
        xp,yp=convert([0,i*n/10,0],obs,theta)
        xp2,yp2=convert([0,i*n/10,n],obs,theta)
        graph.create_line(xp,yp,xp2,yp2,fill="green",width=2)
        #xp,yp=convert([0,-i*n/10,0],obs,theta)
        #xp2,yp2=convert([0,-i*n/10,n],obs,theta)
        #graph.create_line(xp,yp,xp2,yp2,fill="green",width=2)
        xp,yp=convert([i*n/10,n,0],obs,theta)
        xp2,yp2=convert([i*n/10,n,n],obs,theta)
        graph.create_line(xp,yp,xp2,yp2,fill="green",width=2)
        xp,yp=convert([0,i*n/10,0],obs,theta)
        xp2,yp2=convert([n,i*n/10,0],obs,theta)
        graph.create_line(xp,yp,xp2,yp2,fill="green",width=2)
        #xp,yp=convert([0,-i*n/10,0],obs,theta)
        #xp2,yp2=convert([n,-i*n/10,0],obs,theta)
        #graph.create_line(xp,yp,xp2,yp2,fill="green",width=2)

        
        
    for i in range(len(x)-1): #draw lines
        xp,yp=convert([x[i],0,V[i]],obs,theta)
        xp2,yp2=convert([x[i+1],0,V[i+1]],obs,theta)
        graph.create_line(xp,yp,xp2,yp2,fill="yellow",width=2)
        xp,yp=convert([x[i],yr[i],yi[i]],obs,theta)
        xp2,yp2=convert([x[i+1],yr[i+1],yi[i+1]],obs,theta)
        graph.create_line(xp,yp,xp2,yp2,fill="red",width=2)
        xp,yp=convert([x[i],0,p[i]],obs,theta)
        xp2,yp2=convert([x[i+1],0,p[i+1]],obs,theta)
        graph.create_line(xp,yp,xp2,yp2,fill="blue",width=2)
        

    if keyboard.is_pressed("up arrow"):
        obs[1]+=speed
    if keyboard.is_pressed("down arrow"):
        obs[1]-=speed
    if keyboard.is_pressed("left arrow"):
        obs[0]+=speed
    if keyboard.is_pressed("right arrow"):
        obs[0]-=speed
    if keyboard.is_pressed("w"):
        obs[2]+=speed
    if keyboard.is_pressed("s"):
        obs[2]-=speed
    if keyboard.is_pressed("a"):
        phi+=anglespeed
    if keyboard.is_pressed("d"):
        phi-=anglespeed
    if keyboard.is_pressed("i"):
        V[round(len(x)/2)]+=.2
    if keyboard.is_pressed("k"):
        V[round(len(x)/2)]-=.2

    graph.create_text(260,30,text="1-D time dependent Schrodinger equation by Bryce",fill="dark red", font=("Helvetica 14 bold"))
    graph.create_text(235,60,text="Use \"w\",\"s\", and the arrow keys to fly around.",fill="dark red", font=("Helvetica 14 bold"))
    graph.create_text(255,90,text="Use \"i\" and \"k\" to move the middle point manually",fill="yellow", font=("Helvetica 14 bold"))
    graph.create_text(130,200,text="--- wavefunction",fill="red", font=("Helvetica 14 bold"))
    graph.create_text(89,230,text="--- PDF",fill="blue", font=("Helvetica 14 bold"))
    graph.create_text(238,260,text="--- potential energy (infinite boundaries)",fill="yellow", font=("Helvetica 14 bold"))
    root.update()
    graph.delete("all")
    if keyboard.is_pressed("q"):
        cont=0
        root.destroy()











