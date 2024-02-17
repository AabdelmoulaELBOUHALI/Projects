#Champ de pression dans le cas où les pressions sont fixées aux bords_cas général
import numpy as np
from math import *
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

    P=[]


    for i in range (n*m):



        Ux.append(resol[i][0])



        Uy.append(resol[i+n*m][0])

        P.append(resol[i+2*n*m][0])


    return Ux,Uy,P

n=8
m=30
nu=1.83e-5
D=0.5
L=0.2
a=0.5
b=0
c=1
#30,30,1.83e-5,0.5,0.2,0.5,0,1
Ux,Uy,P=U(n,m,nu,D,L,a,b,c)
print(P)

def col_mat(c,m,n):   # m: Nombre de colonne
    N=np.zeros([n,m])
    j=0
    s=0
    N[0][0]=c[0]
    for i in range(n*m):
        if j<n :
            if i%m!=0:
                s+=1
            elif i%m==0 and i>=1:
                s=0
                j+=1
            N[j][s]=c[i]
    return N

A = col_mat(P,m,n)

fig, ax = plt.subplots()#1, 1, figsize=(10, 3))

re=ax.imshow(A, interpolation='bilinear',cmap='autumn_r')
#plt.title("uf')

colorbar_ax = fig.add_axes()
fig.colorbar(re, cax=colorbar_ax,orientation='horizontal')


plt.show()