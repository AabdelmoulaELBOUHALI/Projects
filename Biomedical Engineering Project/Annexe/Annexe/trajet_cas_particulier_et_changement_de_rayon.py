#Programme du mvt du fluide et de la trajectoire_cas particulier de  Poiseuille(Gradient constant)
import numpy as np
import matplotlib.pyplot as plt

R=0.0005 #rayon de la gouttellette

def construction(n,m,x):



    S=np.zeros([n*m,n*m])



    for i in range(m):



        S[i][i]=1



    for i in range(m,n*m-m):



        if (i)%(m)==0:



             S[i][i]=x**2-2*(x**2+1)



             S[i][i+1]=x**2



             S[i][i-(m)]=1



             S[i][i+(m)]=1



        elif (i+1)%(m)==0 :



             S[i][i]=x**2-2*(x**2+1)



             S[i][i-1]=x**2



             S[i][i-(m)]=1



             S[i][i+(m)]=1



        else:



            S[i][i]=-2*(x**2+1)



            S[i][i+1]=x**2



            S[i][i-1]=x**2



            S[i][i-(m)]=1



            S[i][i+m]=1



    for i in range(n*m-m,n*m):



        S[i][i]=1



    return S



def construction1(n,m,r,x):



    A=construction(n,m,r)



    for i in range(m,n*m-m):



        for j in range(n*m):



            A[i][j]=A[i][j]/(x**2)



    return A



def B(n,m,a,b,c):



    A=np.zeros([n*m,1])



    for i in range(n*m):



        if m<=i<n*m-m:



          A[i][0]=a



        elif i<m:



          A[i][0]=b



        else:



          A[i][0]=c



    return A


def resolution(M,B):



    X=np.linalg.solve(M,B)



    return X



#projet 2/



def projet2(n,m,a,b,c,X0,Y0,Vx0,Vy0,dt,D,L):



#n,m,a,b,c la meme pour construction1



#resolution(M,B):en definissan A ET B

    x=L/m

    y=D/n

    r=x/y

    rayon=R

    nu=1.83e-5

    volume=(4*np.pi*rayon**3)/3

    ro=1000

    M=ro*volume



    cte=(3*np.pi*nu*5*rayon)/M



    X = [X0]



    Y = [Y0]



    Vx = [Vx0]



    Vy = [Vy0]



    A = construction1(n,m,r,x)



    C = B(n,m,a,b,c)



    U = resolution(A,C)



    t = 0



    while X[t]<=L and Y[t]<=D and  Y[t]>=0 :



        o = X[t]+dt*Vx[t]



        X.append(o)



        O = Y[t]+dt*Vy[t]



        Y.append(O)



        p = int(X[t+1]/x) #nbr de colonne



        q = int(Y[t+1]/(y)) #nbrs de ligne



        if X[t+1]<=L and Y[t+1]<=D and  Y[t]>=0:



          if X[t+1]%x==0 and Y[t+1]%(y)==0:



            p = int(X[t+1]/x)



            q = int(Y[t+1]/y)



            vitessex = Vx[t] +cte*dt*(U[m*(q-1)+p-1][0]-Vx[t])



            vitessey = Vy[t] -cte*dt*Vy[t]



            Vx.append(vitessex)



            Vy.append(vitessey)



          else :



            p = int(X[t+1]//x)



            q = int(Y[t+1]//y)



            moyenne = (U[m*(q-1)+p-1][0]+U[m*q+p-1][0]+U[m*q+p][0]+U[m*(q-1)+p][0])/4

            vitessex = Vx[t] +cte*dt*(moyenne-Vx[t])



            vitessey = Vy[t]-cte*dt*Vy[t]



            Vx.append(vitessex)



            Vy.append(vitessey)
       

        else:

            X.remove(X[-1])

            Y.remove(Y[-1])

            break



        t = t+1




    return X,Y



#print (projet2(30,30,-0.5,0.5,0.5,0,0.005,0.01,0.03,0.001,0.2,0.5))
#def projet2(n,m,a,b,c,X0,Y0,Vx0,Vy0,dt,M,D,L)
#X,Y=projet2(30,50,-0.5,0.5,0.5,0,0,0.01,0.15,0.001,0.2,0.5)

X,Y=projet2(30,50,-0.5,0.5,0.5,0,0.11,0.01,-0.05,0.001,0.2,0.5)

import matplotlib.pyplot as plt
from numpy import * 
import math

a=0.5   #le longueur du tube principal
b=0.7   # longueur de toute la bifercation
l=0.2   # le diametre du tube pricipal

npx=40
npy=20

o=A=math.atan((l/npy)/(a/npx)) #l'angle en degré
#o=pi*(A/180) #l'angle en radion

pasX=a/npx  # le pas des grids selon les x
pasY=l/npy   # le pas des les grids selon les y

x=linspace(0,a,100) 
y=linspace(a,b,100)

# Les fonctions des bords :
    
def f1(x):
    return l+0*x
    
def f2(x):
    return 0*x
    
def f3(y):
    return tan(o)*(y-a)+l
    
def f4(y):
    return tan(o)*(a-y)
    
z=linspace(a,b,100)

def f5(z):
    return tan(o)*(z-a)+l/2
    
def f6(z):
    return tan(o)*(a-z)+l/2

#les grids de tube principal :
    
def grids(q): #vertical
    u=[]
    w=[]
    for i in arange(0,a,q):
      
        u+=[i,i,i+q,i+q]
        w+=[0,l,l,0]
        
    return u,w
    
def grids0(r): #horizontal
    u=[]
    w=[]
    for i in arange(0,l,r):
        if i<l/2 and i+r<l/2:
            w+=[i,i,i+r,i+r]
            u+=[0,f_6(i),f_6(i+r),0]
        elif i>l/2:
            w+=[i,i,i+r,i+r]
            u+=[0,f_5(i),f_5(i+r),0]
        else :
            w+=[i,i,i,i]
            u+=[0,a,a,0]
    return u,w

#Les fonctions réciproques des fonctions des bords des tubes 1 & 2 :

g=arange(l//2,f3(b),pasY)

def f_3(g):
    return (g-l)/tan(o)+a
    
def f_4(g):
    return -g/tan(o)+a 

def f_5(g):
    return (g-l/2)/tan(o)+a
    
def f_6(g):
    return (l/2-g)/tan(o)+a 

#Les grids du tube 1 :
    
def grids1(q):  #Grids virticaux
    c=[]
    d=[]
    for i in arange(a,b,q):
        c+=[i,i,i+q,i+q]
        d+=[f3(i),f5(i),f5(i+q),f3(i+q)]
    return c,d
    
def grids11(r):  #Grids horizontaux
    m=[]
    n=[]
    for i in arange(l,f3(b),r):
        if i+r<f5(b):
            m+=[i,i,i+r,i+r]
            n+=[f_3(i),f_5(i),f_5(i+r),f_3(i+r)]
        elif i>f5(b):
            m+=[i,i,i+r,i+r]
            n+=[f_3(i),b,b,f_3(i+r)]
        else:
            m+=[i,i,i,i]
            n+=[f_3(i),f_5(i),f_5(i),f_3(i)]
    return n,m
    
#Les grids du tube 2 :
    
def grids2(q): #Grids virticaux 
    c=[]
    d=[]
    for i in arange(a,b,q):
        c+=[i,i,i+q,i+q]
        d+=[f4(i),f6(i),f6(i+q),f4(i+q)]
    return c,d

def grids21(r):  #Grids horizontaux
    m=[]
    n=[]
    for i in arange(0,f4(y[-1]),-r):
        if i-r>f6(b):
            m+=[i,i,i-r,i-r]
            n+=[f_4(i),f_6(i),f_6(i-r),f_4(i-r)]
        elif i<f6(b):
            m+=[i,i,i-r,i-r]
            n+=[f_4(i),b,b,f_4(i-r)]
        else:
            m+=[i,i,i,i]
            n+=[f_4(i),f_6(i),f_6(i),f_4(i)]
    return n,m

#longueur du tube 1 :
lng=((b-a)**2+(f5(b)-l)**2 )**(1/2)
 
print(lng)
    
fig, ax = plt.subplots()

u,w=grids(pasX)
k,p=grids0(pasY)
c,d=grids1(pasX)
e,f=grids2(pasX)
n,m=grids11(pasY)
t,v=grids21(pasY)
plt.plot(u,w,color='#494646')
plt.plot(c,d,color='#494646')
plt.plot(e,f,color='#494646')
plt.plot(n,m,color='#494646')
plt.plot(t,v,color='#494646')
plt.plot(k,p,color='#494646')
plt.plot(x,f1(x),color='black',linewidth=3)
plt.plot(x,f2(x),color='black',linewidth=3)
plt.plot(y,f3(y),color='black',linewidth=3)
plt.plot(y,f4(y),color='black',linewidth=3)
plt.plot(z,f5(z),color='black',linewidth=3)
plt.plot(z,f6(z),color='black',linewidth=3)
#plt.plot(X,Y,color='red',linewidth=3) 
plt.plot(X,Y,color='r',linewidth=4,label='X0=0,Y0=0.11,Vx0=0.01,Vy0=-0.05')
#plt.ylim(f4(b)-pasY,f5(b)+4*pasY)
plt.text(0.15,0.3,"Rayon=0.0005 m")
#plt.yticks(arange(-60,100,pasY))
#plt.xticks(arange(0,b,pasX))
plt.legend()
plt.show()



