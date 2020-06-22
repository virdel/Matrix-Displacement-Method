
import numpy as np



def Informatioan_Processing(path):
    content = []
    data = open(path, 'r')
    for line in data.readlines():
        line = line.replace("\n", "")
        content.append(line)
    data.close()

    # 获取第一行信息
    info = list(eval(content.pop(0)))

    Element_Number = info[0]  # 单元数
    Node_Number = info[1]  # 节点数
    Unknowns = info[2]  # 未知量数
    NumberOfNodeLoad = info[3]  # 节点荷载数
    NumberOfElementLoad = info[4]  # 单元荷载数

    # 节点位置信息
    Node_Position_Info = []
    for i in range(Node_Number):
        Node_Position_Info.append(list(eval(content.pop(0))))
    # 单元信息
    Element_Info = []
    for i in range(int(Element_Number)):
        Element_Info.append(list(eval(content.pop(0))))
    # 定位向量号
    Node_Code = []
    for i in range(Node_Number):
        Node_Code.append(list(eval(content.pop(0))))

    Node_Load_Info = []
    for i in range(NumberOfNodeLoad):
        Node_Load_Info.append(list(eval(content.pop(0))))

    Element_Load_Info = []
    for i in content:
        Element_Load_Info.append(list(eval(i)))

    Node_Position_Info = np.squeeze(np.array([Node_Position_Info]))
    Element_Info = np.squeeze(np.array([Element_Info]))
    Node_Code = np.squeeze(np.array([Node_Code]))
    Node_Load_Info = np.squeeze(np.array([Node_Load_Info]))
    Element_Load_Info = np.squeeze(np.array([Element_Load_Info]))

    return Element_Number, Node_Number, Unknowns,NumberOfNodeLoad, NumberOfElementLoad,Node_Position_Info, Element_Info, Node_Code, Node_Load_Info, Element_Load_Info
