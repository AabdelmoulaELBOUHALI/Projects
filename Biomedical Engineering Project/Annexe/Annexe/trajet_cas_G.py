#Trajectoire de la particule dans le cas général dans un tube
from numpy import *

import pylab as plt

def construction2(n,m,nu,D,L):



    deltay=D/n



    deltax=L/m



    alpha=deltax/deltay



    A=np.zeros([3*n*m,3*n*m])



    for i in range(0,m):



            A[i][i]=1



            A[i+n*m][i+n*m]=1



            A[i+2*n*m][i+2*n*m]=1



    for i in range(m,m*n-m):



        if i%m==0:



            A[i][i]=-2*nu*((alpha**2)+1)+nu



            A[i][i+1]=nu



            A[i][i+m]=nu*alpha**2



            A[i][i-m]=nu*alpha**2



            A[i][2*n*m+i]=deltax/2



            A[i][2*n*m+i+1]=-deltax/2



        elif (i+1)%m==0:



            A[i][i]=-2*nu*((alpha**2)+1)+nu



            A[i][i-1]=nu



            A[i][i+m]=nu*alpha**2



            A[i][i-m]=nu*alpha**2



            A[i][2*n*m+i-1]=deltax/2



            A[i][2*n*m+i]=-deltax/2



        else:



            A[i][i]=-2*nu*((alpha**2)+1)



            A[i][i+1]=nu



            A[i][i-1]=nu



            A[i][i+m]=nu*alpha**2



            A[i][i-m]=nu*alpha**2



            A[i][2*n*m+i-1]=deltax/2



            A[i][2*n*m+i+1]=-deltax/2



    for i in range(m*n-m,m*n):



        A[i][i]=1



        A[i+m*n][i+m*n]=1



        A[i+2*m*n][i+2*m*n]=1



    for i in range(m*n+m,2*m*n-m):



        if i%m==0:



            A[i][i]=-2*nu*((alpha**2)+1)+nu



            A[i][i+1]=nu



            A[i][i+m]=nu*alpha**2



            A[i][i-m]=nu*alpha**2



            A[i][n*m+i+m]=deltax/2



            A[i][n*m+i+1]=-deltax/2



        elif (i+1)%m==0:



            A[i][i]=-2*nu*((alpha**2)+1)+nu



            A[i][i-1]=nu



            A[i][i+m]=nu*alpha**2



            A[i][i-m]=nu*alpha**2



            A[i][n*m+i+m]=alpha*deltax/2



            A[i][n*m+i-m]=-alpha*deltax/2



        else:



            A[i][i]=-2*nu*((alpha**2)+1)



            A[i][i+1]=nu



            A[i][i-1]=nu



            A[i][i+m]=nu*alpha**2



            A[i][i-m]=nu*alpha**2



            A[i][n*m+i+m]=alpha*deltax/2



            A[i][n*m+i-m]=-alpha*deltax/2



    for i in range(2*m*n+m,3*m*n-m):



        if i%m==0:



            A[i][i+1-2*m*n]=1



            A[i][i-2*m*n]=-1



            A[i][i-m-m*n]=alpha



            A[i][i+m-m*n]=-alpha



        elif (i+1)%m:



            A[i][i-2*m*n]=1



            A[i][i-1-2*m*n]=-1



            A[i][i-m-m*n]=alpha



            A[i][i+m-m*n]=-alpha



        else:



            A[i][i+1-2*m*n]=1



            A[i][i-1-2*m*n]=-1



            A[i][i-m-m*n]=alpha



            A[i][i+m-m*n]=-alpha



    return A



def B(n,m,a,b,c):



    L=np.zeros([3*n*m,1])



    for i in range(m):



        L[i][0]=a



        L[m*n-1-i][0]=a



        L[i+m*n][0]=b



        L[2*m*n-1-i][0]=b



        L[i+2*m*n][0]=c



        L[3*m*n-1-i][0]=c



    return L



def resolution2(n,m,nu,D,L,a,b,c):



    M=construction2(n,m,nu,D,L)



    C=B(n,m,a,b,c)



    X=np.linalg.solve(M,C)



    return X



def U(n,m,nu,D,L,a,b,c):



    resol=resolution2(n,m,nu,D,L,a,b,c)



    Ux=[]



    Uy=[]



    for i in range (n*m):



        Ux.append(resol[i][0])



        Uy.append(resol[i+n*m][0])



    return Ux,Uy



#print(U(8,8,1.83e-5,0.2,0.5,0.5,0,0.5))    



#projet 2/



def projet2(n,m,a,b,c,X0,Y0,Vx0,Vy0,dt,D,L):



#n,m,a,b,c la meme pour construction1



#resolution(M,B):en definissan A ET B



    x=L/m



    y=D/n



    r=x/y



    rayon=0.0005



    nu=1.83e-5



    volume=(4*pi*rayon**3)/3



    ro=1000



    M=ro*volume



    cte=(3*pi*nu*5*rayon)/M



    X = [X0]



    Y = [Y0]



    Vx = [Vx0]



    Vy = [Vy0]



    Ux,Uy=U(n,m,nu,D,L,a,b,c)



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



            vitessex = Vx[t] +cte*dt*(Ux[m*(q-1)+p-1]-Vx[t])



            vitessey = Vy[t] +cte*dt*(Uy[m*(q-1)+p-1]-Vy[t])



            Vx.append(vitessex)



            Vy.append(vitessey)



          else :



            p = int(X[t+1]//x)



            q = int(Y[t+1]//y)



            moyennex = (Ux[m*(q-1)+p-1]+Ux[m*q+p-1]+Ux[m*q+p]+Ux[m*(q-1)+p])/4



            moyenney = (Uy[m*(q-1)+p-1]+Uy[m*q+p-1]+Uy[m*q+p]+Uy[m*(q-1)+p])/4



            vitessex = Vx[t] +cte*dt*(moyennex-Vx[t])



            vitessey = Vy[t]+cte*dt*(moyenney-Vy[t])



            Vx.append(vitessex)



            Vy.append(vitessey)



        else:



            X.remove(X[-1])



            Y.remove(Y[-1])



            break



        t = t+1



    return X,Y



# (n,m,a,b,c,X0,Y0,Vx0,Vy0,dt,D,L)

#X0=0,Y0=0.18,Vx0=0.05.,Vy0=-0.025

X,Y=projet2(30,30,0.5,0,1,0,0.18,0.05,-0.025,0.001,0.2,0.5)

a=0.5  
b=0.8 
l=0.2  

npx=30
npy=30

o=A=math.atan((l/npy)/(a/npx)) 
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
    
def grids0(r): #Horizontal
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
    
def grids1(q):  #Grids verticaux
    c=[]
    d=[]
    for i in arange(a,b,q):
        c+=[i,i,i+q,i+q]
        d+=[f3(i),f5(i),f5(i+q),f3(i+q)]
    return c,d
    
def grids11(r):  #Grids horisentaux
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

def grids21(r):  #Grids horisentaux
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
plt.plot(X,Y,color='red',linewidth=3,label='X0=0,Y0=0.18,Vx0=0.05.,Vy0=-0.025')

#plt.ylim(f4(b)+pasY,f5(b)+5*pasY)

#plt.yticks(arange(-60,100,pasY))
#plt.xticks(arange(0,b,pasX))
#plt.grid()

plt.legend()
plt.show()