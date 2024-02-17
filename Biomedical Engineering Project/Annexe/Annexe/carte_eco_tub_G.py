import numpy as np
from math import *

a=0.5
l=0.2

nu=1.9#1.83e-5#1.9
D=l
L=a
n=4
m=10
a,b,c=0.2,0,3333 #a=Vx0 , b=Vy0  , c=Pext   Vx0=0 , Vy0=0 , Pext=333
#construction de la matrice dans le tube (cas général)
#Pressions aux bords fixées
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

            A[i][n*m+i+m]=alpha*deltax/2

            A[i][n*m+i-m]=-alpha*deltax/2

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


def Uxy(n,m,nu,D,L,a,b,c):
    resol=resolution2(n,m,nu,D,L,a,b,c)

    Ux=[]

    Uy=[]

    for i in range (n*m):

        Ux.append(resol[i][0])

        Uy.append(resol[i+n*m][0])

    return Ux,Uy

Ux,Uy=Uxy(n,m,nu,D,L,a,b,c)
print(Ux,Uy)

def x(n,m):
    c=[]
    for i in range(n):
        c+=range(m)
    return c

def y(n,m):
    e=[]
    for i in range(n):
        e+=m*[i]
    return e

fig, ax = plt.subplots()

x_pos=x(n,m)
y_pos=y(n,m)

x_direct = Ux
y_direct = Uy

ax.quiver(x_pos,y_pos,x_direct,y_direct,units='xy',angles='xy',scale=0.4,color='blue')

#plt.xlim(0,a+4*(L/m))
#plt.ylim(-1,l+L/m)
#plt.yticks(np.arange(-1,8,1))
#plt.xticks(np.arange(-1,7,1))
#plt.grid()
plt.legend()
plt.show()
