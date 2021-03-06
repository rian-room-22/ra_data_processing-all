'''
'''

import numpy as np

# ***  ***
def Normalization_dB(Data, FreqPointsNum, Num_of_apectra):
    '''
    Normalizing amplitude-frequency responce (spectra) in dB!!!
    Input parameters:
        Data - input array
        FreqPointsNum - number of frequency channels (data array dimension)
        Num_of_apectra - number of spectra (data array dimension)
    Output parameters:
        Data - result normalized data array
    '''
    DataMinf = []
    DataMinNorm = [0 for col in range(FreqPointsNum)]
    for i in range (FreqPointsNum):
        DataMinf = Data[:, i]                                       # taking 1 line of matrix to find 5 minimum values
        DataMinNorm[i] = np.mean(DataMinf[DataMinf.argsort()[:5]])  # calculating mean of 5 minimum values knowing their indexes

    for k in range (Num_of_apectra):
        with np.errstate(invalid='ignore'):
            Data[k, :] = Data[k, :] - DataMinNorm[:]
    return Data




def Normalization_lin(Data, FreqPointsNum, num_of_spectra):
    '''
    Normalization of amplidude-frequency responce in linear scale!!!
    Input parameters:
        Data - input array
        FreqPointsNum - number of frequency channels (data array dimension)
        Num_of_apectra - number of spectra (data array dimension)
    Output parameters:
        Data - result normalized data array
    '''
    DataMinfind = []
    DataMinNorm = [0 for col in range(FreqPointsNum)]
    for i in range (FreqPointsNum):
        DataMinfind = Data[i, :]    # taking 1 line of matrix to find 5 minimum values
        DataMinNorm[i] = np.mean(DataMinfind[DataMinfind.argsort()[:5]])   # calculating mean of 5 minimum values knowing their indexes

    for k in range (num_of_spectra):
        Data[:, k] = Data[:, k] / DataMinNorm[:]
    return Data
