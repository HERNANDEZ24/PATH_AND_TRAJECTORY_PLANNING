from ctypes import RTLD_GLOBAL
import roboticstoolbox as rtb
import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH

# link lenths in mm
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))
a4 = float(input("a4 = "))

# link mm to meters converter
def mm_to_meter(a):
    m = 1000 # 1 meter = 1000 mm
    return a/m

a1 = mm_to_meter(a1)
a2 = mm_to_meter(a2)
a3 = mm_to_meter(a3)
a4 = mm_to_meter(a4)

# link limits converted to meters
lm1 = float(input("lm1 = "))
lm1 = mm_to_meter(lm1)

lm2 = float(input("lm2 = "))
lm2 = mm_to_meter(lm2)

lm3 = float(input("lm3 = "))
lm3 = mm_to_meter(lm3)

Carte_V3 = DHRobot([
    PrismaticDH(0,0,(270/180)*np.pi,a1,qlim=[0,0]),
    PrismaticDH((270/180)*np.pi,0,(270/180)*np.pi,a2,qlim=[0,lm1]),
    PrismaticDH((270/180)*np.pi,0,(90/180)*np.pi,a3,qlim=[0,lm2]),
    PrismaticDH(0,0,0,a4,qlim=[0,lm3])
],  name='Carte') 

print(Carte_V3)

## q Paths
 # for Carte V3 Joint variables  = ([d1,d2,d3])

q0 = np.array([0,0,0,0])

q1 = np.array([0,mm_to_meter(float(input("d1 = "))),
                mm_to_meter(float(input("d2 = "))),
                mm_to_meter(float(input("d3 = ")))])

#q2 = np.array([0,mm_to_meter(float(input("d1 = "))),
               # mm_to_meter(float(input("d2 = "))),
               # mm_to_meter(float(input("d3 = ")))])

#q3 = np.array([0,mm_to_meter(float(input("d1 = "))),
               # mm_to_meter(float(input("d2 = "))),
               # mm_to_meter(float(input("d3 = ")))])

#q4 = np.array([0,mm_to_meter(float(input("d1 = "))),
               #mm_to_meter(float(input("d2 = "))),
               #mm_to_meter(float(input("d3 = ")))])

# Trajectory commands
traj1 = rtb.jtraj(q0,q1,50)
#traj2 = rtb.jtraj(q1,q2,50)
#traj3 = rtb.jtraj(q2,q3,50)
#traj4 = rtb.jtraj(q3,q4,50)

#plot scale
x1 = -1
x2 = 1
y1 = -1
y2 = 1
z1 = -1
z2 = 1
# for Joint Variable vs Time(S) Table
rtb.qplot (traj1.q)
#rtb.qplot (traj2.q)
#rtb.qplot (traj3.q)

#plot command
Carte_V3.plot(traj1.q,limits= [x1,x2,y1,y2,z1,z2])
#Carte_V3.plot(traj2.q,limits= [x1,x2,y1,y2,z1,z2],movie='Carte_V3_2.gif')
#Carte_V3.plot(traj3.q,limits= [x1,x2,y1,y2,z1,z2],movie='Carte_V3_3.gif')
#Carte_V3.plot(traj4.q,limits= [x1,x2,y1,y2,z1,z2],movie='Carte_V3_4.gif')

Carte_V3.teach(jointlabels=1)
