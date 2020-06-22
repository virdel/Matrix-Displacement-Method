import math
import numpy as np
from ETM import ELEMENT_TRANSFER_MATRIX
from TM import TRANSFER_MATRIX
def LSC(Start_node_code,End_node_code,Element_positioning_vector, Node_Position_Info,Unknowns):

    P1=Node_Position_Info[Start_node_code-1]
    P2=Node_Position_Info[End_node_code-1]
    P3=P2-P1
    L=math.hypot(P3[0],P3[1])
    sin=P3[1]/L
    cos=P3[0]/L
    T=ELEMENT_TRANSFER_MATRIX(sin,cos)
    S=TRANSFER_MATRIX(Element_positioning_vector,Unknowns)
    S = S.astype(np.int16)
    return L,sin,cos,T,S