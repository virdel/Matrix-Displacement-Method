import  numpy as np

#形成单元刚度矩阵
def ESM(E,A,ZI,BL):
    '''
    :param E: 弹性模量
    :param A: 截面面积
    :param ZI: 惯性矩
    :param BL: 长度
    :return: EK
    '''

    EK=np.zeros((6,6))
    EK[0,0]=E*A/BL
    EK[0,3]=-EK[0,0]
    EK[1,1]=12*E*ZI/pow(BL,3)
    EK[1,2]=6*E*ZI/BL/BL
    EK[1,4]=-EK[1,1]
    EK[1,5]=EK[1,2]
    EK[2,2]=4*E*ZI/BL
    EK[2,4]=-EK[1,2]
    EK[2,5]=2*E*ZI/BL
    EK[3,3]=EK[0,0]
    EK[4,4]=EK[1,1]
    EK[4,5]=EK[2,4]
    EK[5,5]=EK[2,2]

    EK=EK+EK.T-np.diag(EK.diagonal())

    return EK
