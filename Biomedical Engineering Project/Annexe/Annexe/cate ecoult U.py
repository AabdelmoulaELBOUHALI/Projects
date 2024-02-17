#carte d'écoulment dans un tube (cas particulier de Poiseuille)
import numpy as np
import matplotlib.pyplot as plt

m=22
n=14

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

def u(n,m,U):
    V=[]
    for i in range(n*m):
        if len(V)<=n*m:
            V.append(U[i][0])
    return V

x_direct = u(n,m,U)
y_direct = (n*m)*[0]

ax.quiver(x_pos,y_pos,x_direct,y_direct,units='xy',angles='xy',scale=50,color='blue')
plt.title('grad(P)/nu=-3')

print(U)
plt.xlim(0,8)
plt.yticks(np.arange(-1,8,1))
plt.xticks(np.arange(-1,7,1))
plt.grid()

plt.show()





