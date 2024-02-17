import numpy as np
from math import *

#******A supprimer

def construction3(n1,m1,L,l,D,o,nu):

    deltax1=L/(m1-1)

    deltay=D/(n1-1)

    deltax2=deltay/tan(o)

    m2=int(l*cos(o)/deltax2)

    m=int(m1+m2)

    n=int(n1+2*m2)

    A=np.zeros([3*n*m,3*n*m])

    for j in range(m2+1):

        for i in range(j*m,(j+1)*m-j):

            A[i][i]=1

            A[i+m*n][i+m*n]=1

            A[i+2*m*n][i+2*m*n]=1

    for j in range(m2+1):

        for i in range(m*(m2+n1-1)+j*m,m*(m2+n1-1)+j*m+m1+j):

            A[i][i]=1

            A[i+m*n][i+m*n]=1

            A[i+2*m*n][i+2*m*n]=1

    p=int(m2+((n1+1)/2))*m-m2-1#milieu

    for j in range(m2+1):

        for i in range(p-m*j+j,p-m*j+j+m2-j+1):

            A[i][i]=1

            A[i+m*n][i+m*n]=1

            A[i+2*m*n][i+2*m*n]=1

        for k in range(p+m*j+j,p+m*j+j+m2-j+1):

            A[k][k]=1

            A[k+m*n][k+m*n]=1

            A[k+2*m*n][k+2*m*n]=1



    for i in range(m*n):

        if A[i][i]==0:

            if i%m==0:

                alpha=deltax1/deltay

                A[i][i]=-2*nu*((alpha**2)+1)+nu

                A[i][i+1]=nu

                A[i][i+m]=nu*alpha**2

                A[i][i-m]=nu*alpha**2

                A[i][2*n*m+i]=deltax1/2

                A[i][2*n*m+i+1]=-deltax1/2

            elif (i+1)%m==0:

                alpha=deltax2/deltay

                A[i][i]=-2*nu*((alpha**2)+1)+nu

                A[i][i-1]=nu

                A[i][i+m]=nu*alpha**2

                A[i][i-m]=nu*alpha**2

                A[i][2*n*m+i-1]=deltax2/2

                A[i][2*n*m+i]=-deltax2/2

            elif i%(m1-1)==0:

                A[i][i]=2*nu*((-deltax1-deltax2)/(deltax1*deltax2*(deltax1+deltax2))-1/(deltay)**2)

                A[i][i+1]=(2*nu*deltax2)/((deltax1+deltax2)*deltax1*deltax2)

                A[i][i-1]=(2*nu*deltax2)/((deltax1+deltax2)*deltax1*deltax2)

                A[i][i+m]=1/((deltay)**2)

                A[i][i-m]=1/((deltay)**2)

                A[i][2*n*m+i-1]=-1/(deltax1+deltax2)

                A[i][2*n*m+i+1]=1/(deltax1+deltax2)

    for i in range(n):

        for j in range(m):

            if A[i*m+j][i*m+j]==0:

                if j<m1-1:

                    alpha=deltax1/deltay

                    A[i*m+j][i*m+j]=-2*nu*((alpha**2)+1)

                    A[i*m+j][i*m+j+1]=nu

                    A[i*m+j][i*m+j-1]=nu

                    A[i*m+j][i*m+j+m]=nu*alpha**2

                    A[i*m+j][i*m+j-m]=nu*alpha**2

                    A[i*m+j][2*n*m+i*m+j-1]=deltax1/2

                    A[i*m+j][2*n*m+i*m+j+1]=-deltax1/2

                elif j>(m1-1):

                    alpha=deltax2/deltay

                    A[i*m+j][i*m+j]=-2*nu*((alpha**2)+1)

                    A[i*m+j][i*m+j+1]=nu

                    A[i*m+j][i*m+j-1]=nu

                    A[i*m+j][i*m+j+m]=nu*alpha**2

                    A[i*m+j][i*m+j-m]=nu*alpha**2

                    A[i*m+j][2*n*m+i*m+j-1]=deltax2/2

                    A[i*m+j][2*n*m+i*m+j+1]=-deltax2/2

    for i in range(m*n,2*m*n):

        if A[i][i]==0:

            if i%m==0:

                alpha=deltax1/deltay

                A[i][i]=-2*nu*((alpha**2)+1)+nu

                A[i][i+1]=nu

                A[i][i+m]=nu*alpha**2

                A[i][i-m]=nu*alpha**2

                A[i][n*m+i+m]=deltax1/2

                A[i][n*m+i+1]=-deltax1/2

            elif (i+1)%m==0:

                alpha=deltax2/deltay

                A[i][i]=-2*nu*((alpha**2)+1)+nu

                A[i][i-1]=nu

                A[i][i+m]=nu*alpha**2

                A[i][i-m]=nu*alpha**2

                A[i][n*m+i+m]=alpha*deltax2/2

                A[i][n*m+i-m]=-alpha*deltax2/2

            elif i%(m1-1)==0:

                A[i][i]=2*nu*((-deltax1-deltax2)/(deltax1*deltax2*(deltax1+deltax2))-1/(deltay)**2)

                A[i][i+1]=(2*nu*deltax2)/((deltax1+deltax2)*deltax1*deltax2)

                A[i][i-1]=(2*nu*deltax2)/((deltax1+deltax2)*deltax1*deltax2)

                A[i][i+m]=1/((deltay)**2)

                A[i][i-m]=1/((deltay)**2)

                A[i][n*m+i-m]=-1/2*deltay

                A[i][n*m+i+m]=1/2*deltay

    for i in range(n):

        for j in range(m):

            if A[i*m+j+n*m][i*m+j+n*m]==0:

                if j<m1-1:

                    alpha=deltax1/deltay

                    A[i*m+j+m*n][i*m+j+m*n]=-2*nu*((alpha**2)+1)

                    A[i*m+j+m*n][i*m+j+m*n+1]=nu

                    A[i*m+j+m*n][i*m+j+m*n-1]=nu

                    A[i*m+j+m*n][i*m+j+m*n+m]=nu*alpha**2

                    A[i*m+j+m*n][i*m+j+m*n-m]=nu*alpha**2

                    A[i*m+j+m*n][n*m+i*m+j+n*m-m]=1/2*deltay

                    A[i*m+j+m*n][n*m+i*m+j+m*n+m]=1/2*deltay

                elif j>(m1-1):

                    alpha=deltax2/deltay

                    A[i*m+j+m*n][i*m+j+m*n]=-2*nu*((alpha**2)+1)

                    A[i*m+j+m*n][i*m+j+m*n+1]=nu

                    A[i*m+j+m*n][i*m+j+m*n-1]=nu

                    A[i*m+j+m*n][i*m+j+m*n+m]=nu*alpha**2

                    A[i*m+j+m*n][i*m+j+m*n-m]=nu*alpha**2

                    A[i*m+j+m*n][n*m+i*m+j+n*m-m]=1/2*deltay

                    A[i*m+j+m*n][n*m+i*m+j+m*n+m]=1/2*deltay

    for i in range(2*n*m,3*n*m):

        if A[i][i]==0:

            if i%m==0:

                A[i][i+1-2*m*n]=1/(deltax1+deltax2)

                A[i][i-2*m*n]=-1/(deltax1+deltax2)

                A[i][i-m-m*n]=1/2*deltay

                A[i][i+m-m*n]=-1/2*deltay

            elif (i+1)%m:

                A[i][i-2*m*n]=1/(deltax1+deltax2)

                A[i][i-1-2*m*n]=-1/(deltax1+deltax2)

                A[i][i-m-m*n]=1/2*deltay

                A[i][i+m-m*n]=-1/2*deltay



    for i in range(n):

        for j in range(m):

            if A[i*m+j+2*n*m][i*m+j+2*n*m]==0:

                if j<m1-1:

                    alpha=deltax1/deltay

                    A[i*m+j+2*n*m][i*m+j+2*n*m+1-2*m*n]=1

                    A[i*m+j+2*n*m][i*m+j+2*n*m-1-2*m*n]=-1

                    A[i*m+j+2*n*m][i*m+j+2*n*m-m-m*n]=alpha

                    A[i*m+j+2*n*m][i*m+j+2*n*m+m-m*n]=-alpha

                elif j>m1-1:

                    alpha=deltax2/deltay

                    A[i*m+j+2*n*m][i*m+j+2*n*m+1-2*m*n]=1

                    A[i*m+j+2*n*m][i*m+j+2*n*m-1-2*m*n]=-1

                    A[i*m+j+2*n*m][i*m+j+2*n*m-m-m*n]=alpha

                    A[i*m+j+2*n*m][i*m+j+2*n*m+m-m*n]=-alpha

    return A



A=construction3(3,3,2,1,1,pi/4,1.9)

def B3(n1,m1,L,l,D,o,nu,a,b,c):

    deltax1=L/(m1-1)

    deltay=D/(n1-1)

    deltax2=deltay/tan(o)

    m2=int(l*cos(o)/deltax2)

    m=int(m1+m2)

    n=int(n1+2*m2)

    B=np.zeros([3*n*m,1])

    for j in range(m2+1):

        for i in range(j*m,(j+1)*m-j):

            if i==(j+1)*m-j-1:

                B[i][0]=a

                B[i+n*m][0]=b

                B[i+2*n*m][0]=c

            elif i>=m2*m:

                B[i][0]=a

                B[i+n*m][0]=b

                B[i+2*n*m][0]=c

    for j in range(m2+1):

        for i in range(m*(m2+n1-1)+j*m,m*(m2+n1-1)+j*m+m1+j):

            if i==m*(m2+n1-1)+j*m+m1+j-1:

                B[i][0]=a

                B[i+n*m][0]=b

                B[i+2*n*m][0]=c

            elif (n1-1+m2)*m<=i<=(n1-1+m2)*m-1:

                B[i][0]=a

                B[i+n*m][0]=b

                B[i+2*n*m][0]=c

    p=int(m2+((n1+1)/2))*m-m2-1#milieu

    for j in range(m2+1):

        for i in range(p-m*j+j,p-m*j+j+m2-j+1):

            if i==p-m*j+j:

                B[i][0]=a

                B[i+n*m][0]=b

                B[i+2*n*m][0]=c

        for k in range(p+m*j+j,p+m*j+j+m2-j+1):

            if i==p-m*j+j:

                B[i][0]=a

                B[i+n*m][0]=b

                B[i+2*n*m][0]=c

    return B

#print(B3(3,3,2,1,1,pi/4,1.9,1,1,1))

def resolution3(n1,m1,L,l,D,o,nu,a,b,c):

    A=construction3(n1,m1,L,l,D,o,nu)

    B=B3(n1,m1,L,l,D,o,nu,a,b,c)

    X=np.linalg.solve(A,B)

    return X

print(resolution3(3,3,2,1,1,pi/4,1.9,1,1,1))