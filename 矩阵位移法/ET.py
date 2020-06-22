import  numpy as np

def ELEMENT_TRANSFER_MATRIX(sin,cos):
    T=np.zeros([6,6])
    T[0,0]=cos
    T[0,1]=sin
    T[1,0]=-sin
    T[1,1]=cos
    T[2,2]=1
    T[3,3]=cos
    T[3,4]=sin
    T[4,3]=-sin
    T[4,4]=cos
    T[5,5]=1
    return T