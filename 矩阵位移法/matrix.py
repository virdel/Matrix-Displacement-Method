import  numpy as np
import math
from ESM import ESM
from INFORMATION_PROCESSING import Informatioan_Processing
from LSC  import LSC
from EFF import EFF
Element_Number, Node_Number,Unknowns,NumberOfNodeLoad, NumberOfElementLoad,\
Node_Position_Info, Element_Info, Node_Code, Node_Load_Info, Element_Load_Info\
    =Informatioan_Processing("1.txt")



## 总刚清零
TK=np.zeros((Unknowns,Unknowns))


#荷载向量清零
P=np.zeros((Unknowns,1))

#处理节点力
if(NumberOfNodeLoad):
    def NODE_Load(P,Node_Load_Info):
        for i in Node_Load_Info:
            P[ Node_Code[i[0]-1,i[1]-1]-1]=i[2]
        return P

    P=NODE_Load(P,Node_Load_Info)

Element_positioning_vectors=[]
Ls=[]
Ts=[]
Ss=[]
for i in range(Element_Number):

    Start_node_code = Element_Info[i, 0]#起始节点号
    End_node_code = Element_Info[i, 1]#末端节点号
    # 单元定位向量
    Element_positioning_vector= np.concatenate(( Node_Code[Start_node_code - 1],  Node_Code[End_node_code - 1]))
    #形成单元常数:L,sin,cos,S,T
    L,sin,cos,S,T=LSC(Start_node_code,End_node_code,Element_positioning_vector, Node_Position_Info,Unknowns)
    Element_positioning_vectors.append(Element_positioning_vector)
    Ls.append(L)
    Ts.append(T)
    Ss.append(S)
    #形成单元坐标系下单刚
    EK=ESM(Element_Info[i,2],Element_Info[i,3],Element_Info[i,4],L)

    #结构坐标系下单刚
    EK=np.dot(np.dot(T.T,EK),T)
    #集成总刚
    TK=TK+np.dot(np.dot(S,EK),S.T)
    #单元固端力：EFF


    #单元等效力

    #综合荷载向量

if NumberOfElementLoad>0:
    P=P+EFF(Element_Load_Info,Unknowns,Ls,Ts,Ss)




#解方程
print(TK)
x=np.linalg.solve(TK,P)
print(x)
#输出单元力
