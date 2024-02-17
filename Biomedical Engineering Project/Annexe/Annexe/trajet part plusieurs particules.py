import numpy as np
import matplotlib.pyplot as plt
from numpy import * 

ab=0.2  #decalage suivant les x>=0
a=0.5
A=ab+a   #abscisse du pt d'inflexion
B=0.3
l=0.2    # le diamètre du tube principal
b=a+B   # abscisse du dernier pt 

npx=50
npy=30

o=math.atan((l/npy)/(a/npx)) 
#o=pi*(A/180) #l'angle en radion

cd=(b-a)*np.tan(o) #décalage suivant les y positives

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
    
def f4(y):
    return tan(o)*(ab+a-y)+cd
    
z=linspace(a+ab,b+ab,100)

def f5(z):
    return tan(o)*(z-a-ab)+l/2+cd
    
def f6(z):
    return tan(o)*(ab+a-z)+l/2+cd


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



#sous-projet 2/_trajectoire de la particule



def projet2(n,m,a,b,c,X0,Y0,Vx0,Vy0,dt,D,L):



#n,m,a,b,c les memes pour construction1



#résolution(M,B):en définissant A ET B

    x=L/m

    y=D/n

    r=x/y

    rayon=0.0005

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



        #else :



         #    break  

       

        else:

            X.remove(X[-1])

            Y.remove(Y[-1])

            break



        t = t+1






    return X,Y



#print (projet2(30,30,-0.5,0.5,0.5,0,0.005,0.01,0.03,0.001,0.2,0.5))

#def projet2(n,m,a,b,c,X0,Y0,Vx0,Vy0,dt,M,D,L)

X,Y=projet2(30,50,-0.5,0.5,0.5,(0+ab),(0+cd),0.01,0.15,0.001,(0.2+cd),(0.5+ab))
X1,Y1=projet2(30,50,-0.5,0.5,0.5,(0+ab),(0.03+cd),0.01,0.05,0.001,(0.2+cd),(0.5+ab))
X2,Y2=projet2(30,50,-0.5,0.5,0.5,(0+ab),(0.19+cd),0.01,-0.18,0.001,(0.2+cd),(0.5+ab))
X3,Y3=projet2(30,50,-0.5,0.5,0.5,(0+ab),(0.1+cd),0.01,0,0.001,(0.2+cd),(0.5+ab))
X4,Y4=projet2(30,50,-0.5,0.5,0.5,(0+ab),(0+cd),0.01,0.15,0.001,(0.2+cd),(0.5+ab))
X5,Y5=projet2(30,50,-0.5,0.5,0.5,(0+ab),(0+cd),0.01,0.3,0.001,(0.2+cd),(0.5+ab))

#les grids de tube principal :
    
def grids(q): #vertical
    u=[]
    w=[]
    for i in arange(ab,a+ab,q):
        u+=[i,i,i+q,i+q]
        w+=[cd,l+cd,l+cd,cd]
    return u,w
    
def grids0(r): #Horizontal
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

#Les grids du tube 1 (au dessus):
    
def grids1(q):  #Grids verticaux
    c=[]
    d=[]
    for i in arange(a+ab,b+ab,q):
        c+=[i,i,i+q,i+q]
        d+=[f3(i),f5(i),f5(i+q),f3(i+q)]
    return c,d
    
def grids11(r):  #Grids horizentaux
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
    
#Les grids de le tube 2 (en dessous):
    
def grids2(q): #Grids virticaux
    c=[]
    d=[]
    for i in arange(a+ab,b+ab,q):
        c+=[i,i,i+q,i+q]
        d+=[f4(i),f6(i),f6(i+q),f4(i+q)]
    return c,d

def grids21(r):  #Grids horizontaux
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

#longueur du tube 1 :
lng=((b-a)**2+(f5(b+ab)-l)**2 )**(1/2)
 
print(lng)

#def projet2(n,m,a,b,c,X0,Y0,Vx0,Vy0,dt,M,D,L)

#X,Y=projet2(30,50,-0.5,0.5,0.5,0,0,0.01,0.15,0.001,0.2,0.5)

    
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
plt.plot(X,Y,color='red',linewidth=5,label='X0=0,Y0=0,Vx0=0.01,Vy0=0.15')
plt.plot(X1,Y1,linewidth=4,label='X0=0,Y0=0.03,Vx0=0.01,Vy0=0.05')
plt.plot(X2,Y2,color='yellow',linewidth=3,label='X0=0,Y0=0.19,Vx0=0.01,Vy0=-0.001')
plt.plot(X3,Y3,linewidth=4,label='X0=0,Y0=0.1,Vx0=0.01,Vy0=0.001')
plt.plot(X4,Y4,linewidth=4,label='X0=0,Y0=0,Vx0=0.01,Vy0=0.015')
plt.plot(X5,Y5,linewidth=4,label='X0=0,Y0=0,Vx0=0.2,Vy0=0.3')

plt.ylim(0,f3(b+ab)+5*pasY)
plt.xlim(0,ab+b+pasX)
#plt.yticks(arange(-60,100,pasY))
#plt.xticks(arange(0,b,pasX))
#plt.grid()
plt.legend(loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)

plt.show() 