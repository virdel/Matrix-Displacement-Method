import  numpy as np

def EFF(Element_Load_Info,Unknowns,Ls,Ts,Ss):
    Fe=np.zeros((Unknowns,1))
    for i in Element_Load_Info:
        FO=np.zeros((6,1))
        type=i[1]
        G=i[1]
        c=i[3]
        T=Ts[i[0]-1]
        S=Ss[i[0]-1]

        l=Ls[i[0]-1]
        b = l - c


        if type==1:
            FO[1]=-G*c*(1-pow(c/l,2)+0.5*pow(c/l,3))
            FO[2]=-G*c*c/12*(6-8*c/l+3*pow(c/l,2))
            FO[4]=-G*c*c*c/l/l*(1-0.5*c/l)
            FO[5]=G*c*c*c/12/l*(4-3*c/l)
        elif     type==2:
            FO[1]=-G*pow(b/l,2)*(1+2*c/l)
            FO[2]=-G*c*b*b/l/l
            FO[4]=-G*pow(c/l,2)*(1+2*b/l)
            FO[5]=G*c*c*b/l/l

        elif type==3:
            FO[1]=G*6*c*b/l/l/l
            FO[2]=G*b/l*(2-3*b/l)
            FO[4]=-G*6*c*b/l/l/l
            FO[5]=G*c/l*(2-3*c/l)

        FO=-np.dot(T.T,FO)
        Fe=Fe+np.dot(S,FO)

    return Fe
