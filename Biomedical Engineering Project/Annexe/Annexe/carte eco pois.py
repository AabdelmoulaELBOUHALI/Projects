import numpy as np
import matplotlib.pyplot as plt

m=20
n=15

m1=10
m2=m-m1

n1=n//2

n3=n1+(n%2)

l=40

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
#equation tub principal :
A1=construction1(n,m1,1,1)
B1=B(n,m1,-3,0,0)
U1=resolution(A1,B1)
#equation tub 2 :
A2=construction1(n3,m2,1,1)
B2=B(n3,m2,-5 ,50,0)
U2=resolution(A2,B2)
#equation tub 1 :
A3=construction1(n3,m2,1,1)
B3=B(n3,m2,-5,0,50)
U3=resolution(A3,B3)

    
#ajouter les vrais conditions :
U3[(n3-1)*m2:n3*m2]=m2*[[0]]
U2[0:m2]=m2*[[0]]

#Les abssaices :
def x(n,m):
    c=[]
    for i in range(n):
        c+=range(m1)
    for i in range(n+(n%2)):
        c+=range(m1,m)
    return c
    
#les ordonnées : 
def y(n,m):
    e=[]
    for i in range(n):
        if len(e)<=m1*n:
            e+=m1*[i]
    for i in range(n+(n%2)):
        if i>=n3:
            e+=range(i,m2+i)
        elif i<=n1:
            e+=range(i,i-m2,-1)
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

x_direct=u(n,m1,U1)
x_direct+=u(n3,m2,U3*np.cos(-np.pi/4))
x_direct+=u(n1,m2,U2*np.cos(np.pi/4))
x_direct+=(n%2)*m2*[0]
y_direct=(n*m1)*[0]
y_direct+=u(n3,m2,U3*np.sin(-np.pi/4))
y_direct+=u(n1,m2,U2*np.sin(np.pi/4))
y_direct+=(n%2)*m2*[0]

ax.quiver(x_pos,y_pos,x_direct,y_direct,units='xy',angles='xy',scale=50,color='blue')
plt.title('Branche pricipale: gradP/nu=-3 \n Branche secondaire: gradP/nu=-5',color='green',fontsize=16) 

#print(U)
#plt.xlim(0,8)
#plt.yticks(np.arange(-1,10,1))
#plt.xticks(np.arange(-1,22,1))
#plt.grid()

plt.show()





