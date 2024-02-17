from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt

m=30  # nombre de colonnes
n=20  #nombre de lignes
#construction de la matrice M dans un tube (gradP=cste)
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

A=construction1(n,m,1,1)
B=B(n,m,-3,0,0)
U=resolution(A,B)

print(U)

def u(n,m,U): #Fonction pour changer la matrice colonne à une liste
    V=[]
    for i in range(n*m):
        if len(V)<=n*m:
            V.append(U[i][0])
    return V

N=u(n,m,U)

#fonction pour transformer une liste en une matrice de taille n*m à donner
def col_mat(c,m,n):   # m: Nombre de colonne  c: la liste qu'on veut transformer
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

A = col_mat(N,m,n) # la matrice des valeurs

fig, ax = plt.subplots() #Construction de plusieurs graphes en meme temps

re=ax.imshow(A, interpolation='bilinear',cmap='winter_r') #instruction de tracage de la matrice

colorbar_ax = fig.add_axes() #instruction de construction la barre des valeurs
fig.colorbar(re, cax=colorbar_ax,orientation='horizontal') #instruction de tracage de la barre


plt.show()