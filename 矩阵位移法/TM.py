import numpy as np


def TRANSFER_MATRIX(CODE_D_NOD, N):
    """

    :param CODE_D_NOD: 
    :param N: 
    :return: 
    """

    S = np.zeros((N, 6), dtype=np.int16)
    for i in range(6):
        if CODE_D_NOD[i] > 0:
            S[CODE_D_NOD[i] - 1, i] = 1
    return S
