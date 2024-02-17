#trajectoire_animation
import numpy as np
import matplotlib.pyplot as plt



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



       # if m*(p-1)+q-1<n*m and m*(p-1)+q<n*m and m*p+q<n*m and m*p+q-1<n*m and m*(p-1)+q-1>0 and m*(p-1)+q>0 and m*p+q-1>0 and m*p+q>0:

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



    #F = (Y[-2]+Y[-1])/2



    #X.remove(X[-1])



    #Y.remove(Y[-1])



    #f = (m-1)*x



    #X.append(f)



    #Y.append(F)



    return X,Y



#print (projet2(30,30,-0.5,0.5,0.5,0,0.005,0.01,0.03,0.001,0.2,0.5))

#def projet2(n,m,a,b,c,X0,Y0,Vx0,Vy0,dt,M,D,L)

X,Y=projet2(30,50,-0.5,0.5,0.5,0,0,0.01,0.15,0.001,0.2,0.5)

import matplotlib.animation as animation

x = X
y = Y

fig, ax = plt.subplots()
line, = ax.plot(x, y, color='r')

def update(num, x, y, line):
    line.set_data(x[:num], y[:num])
    #line.axes.axis([0, 10, 0, 1])
    return line,

ani = animation.FuncAnimation(fig, update, len(x), fargs=[x, y, line],
                              interval=0.000001, blit=True)

plt.show()
