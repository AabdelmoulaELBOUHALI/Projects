#Maillage de la bifurcation
import matplotlib.pyplot as plt
from numpy import * 
import math

a=30   #La longueur de la trachée
b=40    # La longueur de al btfurcation
l=60   # le diametre du tube pricipal
ab=0  #decalage suivant les x positifs

npx=30
npy=20

o=math.atan((l/npy)/(a/npx))
#o=pi*(A/180) #l'angle en radion

cd=(b-a)*tan(o) #decalage suivant les y positifs 

pasX=a/npx  # le pas des grids selon les x
pasY=l/npy   # le pas des les grids selon les y

x=linspace(ab,a+ab,100) 
y=linspace(a+ab,b+ab,100)

# Les fonctions des bords :
    
def f1(x):
    return cd+l+0*x
    
def f2(x):
    return 0*x+cd
    
def f3(y):
    return tan(o)*(y-a-ab)+l+cd
    de 
def f4(y):
    return tan(o)*(ab+a-y)+cd
    
z=linspace(a+ab,b+ab,100)

def f5(z):
    return tan(o)*(z-a-ab)+l/2+cd
    
def f6(z):
    return tan(o)*(ab+a-z)+l/2+cd

#les grids de tube principal :
    
def grids(q): #verticaux
    u=[]
    w=[]
    for i in arange(ab,a+ab,q):
        u+=[i,i,i+q,i+q]
        w+=[cd,l+cd,l+cd,cd]
       
    return u,w
    
def grids0(r): #horizontaux
    u=[]
    w=[]
    for i in arange(cd,l+cd,r):
        if i<l/2+cd and i+r<l/2+cd:
            w+=[i,i,i+r,i+r]
            u+=[ab,f_6(i),f_6(i+r),ab]
        elif i>l/2+cd:
            w+=[i,i,i+r,i+r]
            u+=[ab,f_5(i),f_5(i+r),ab]
        else :
            w+=[i,i,i,i]
            u+=[ab,a+ab,a+ab,ab]
    return u,w

#Les fonctions réciproques des fonctions des bords des tubes 1 & 2 :

g=arange(cd+l//2,f3(b+ab),pasY)

def f_3(g):
    return (g-l-cd)/tan(o)+a+ab
    
def f_4(g):
    return (-g+cd)/tan(o)+a+ab 

def f_5(g):
    return (g-l/2-cd)/tan(o)+a+ab
    
def f_6(g):
    return (cd+l/2-g)/tan(o)+a+ab 

#Les grids du tube 1 :
    
def grids1(q):  #Grids verticaux
    c=[]
    d=[]
    for i in arange(a+ab,b+ab,q):
        c+=[i,i,i+q,i+q]
        d+=[f3(i),f5(i),f5(i+q),f3(i+q)]
    return c,d
    
def grids11(r):  #Grids horizontaux
    m=[]
    n=[]
    for i in arange(l+cd,f3(b+ab),r):
        if i+r<f5(b+ab):
            m+=[i,i,i+r,i+r]
            n+=[f_3(i),f_5(i),f_5(i+r),f_3(i+r)]
        elif i>f5(b+ab):
            m+=[i,i,i+r,i+r]
            n+=[f_3(i),ab+b,ab+b,f_3(i+r)]
        else:
            m+=[i,i,i,i]
            n+=[f_3(i),f_5(i),f_5(i),f_3(i)]
    return n,m
    
#Les grids de le tube 2 :
    
def grids2(q): #Grids virticaux
    c=[]
    d=[]
    for i in arange(a+ab,b+ab,q):
        c+=[i,i,i+q,i+q]
        d+=[f4(i),f6(i),f6(i+q),f4(i+q)]
    return c,d

def grids21(r):  #Grids horisentaux
    m=[]
    n=[]
    for i in arange(cd,f4(y[-1]),-r):
        if i-r>f6(b+ab):
            m+=[i,i,i-r,i-r]
            n+=[f_4(i),f_6(i),f_6(i-r),f_4(i-r)]
        elif i<f6(b+ab):
            m+=[i,i,i-r,i-r]
            n+=[f_4(i),b+ab,b+ab,f_4(i-r)]
        else:
            m+=[i,i,i,i]
            n+=[f_4(i),f_6(i),f_6(i),f_4(i)]
    return n,m

#londeur du tube 1 :
lng=((b-a)**2+(f5(b+ab)-l)**2 )**(1/2)
 
print(lng)
    
fig, ax = plt.subplots()

u,w=grids(pasX)
k,p=grids0(pasY)
c,d=grids1(pasX)
e,f=grids2(pasX)
n,m=grids11(pasY)
t,v=grids21(pasY)
plt.plot(x,f1(x),color='black',linewidth=3)
plt.plot(x,f2(x),color='black',linewidth=3)
plt.plot(y,f3(y),color='black',linewidth=3)
plt.plot(y,f4(y),color='black',linewidth=3)
plt.plot(z,f5(z),color='black',linewidth=3)
plt.plot(z,f6(z),color='black',linewidth=3)
plt.plot(u,w,color='black')
plt.plot(c,d,color='black')
plt.plot(e,f,color='black')
plt.plot(n,m,color='black')
plt.plot(t,v,color='black')
plt.plot(k,p,color='black')

plt.ylim(0,f3(b+ab)+5*pasY)
plt.xlim(0,ab+b+pasX)


plt.show() 