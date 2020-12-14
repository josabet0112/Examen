import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 80, 0, 80])

plt.axis('on')
plt.grid(True)





#hacer un circulo morado con centro 20,20 con radio r=50

xc=30
yc=30
r=5

P1=0*np.pi/180
p2=360*np.pi/180
dp=(p2-P1)/100

xlast=xc+r*np.cos(P1)
ylast=yc+r*np.sin(P1)

for p in np.arange(P1,p2+dp,dp):
    x=xc+r*np.cos(p)
    y=yc+r*np.sin(p)
    plt.plot([xlast,x],[ylast,y],color='purple',linewidth=2)
    xlast=x
    ylast=y

# Dibujamos el primer rectangulo
Ax = 30
Ay = 30
Bx = 20
By = 30
Cx = 20
Cy = 20
Dx = 30
Dy = 20

xp = [Ax, Bx, Cx, Dx, Ax]
yp = [Ay, By,  Cy, Dy, Ay]
plt.plot(xp, yp, color='b')

# Dibujamos el segundo rectangulo
Ax = 35
Ay = 35
Bx = 25
By = 35
Cx = 25
Cy = 25
Dx = 35
Dy = 25

xp = [Ax, Bx, Cx, Dx, Ax]
yp = [Ay, By,  Cy, Dy, Ay]
plt.plot(xp, yp, color='r')

    
plt.show()