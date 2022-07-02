# Objetivo: Comparar o tempo de processamento de um código sequencial e um código processamento paralelo
# 
# Fluxo do código: Será construído um array com 1000000 elementos e será feita a soma de todos os elementos
# do array através de processamento sequencial e processamento paralelo.

#----------------------------------------------------------------------------------------------------------------
# A classe Process é utilizada para fazer o processamento paralelo
# Para criar o array importamos o módulo empty
# E, por fim, usaremos a biblioteca time para calcular o tempo de processamento. 
from multiprocessing import Process 
from numpy import empty
import time

from pandas import array

# ----------------------------------------------------------------------------------------------------------------
class ParameterSum():
    def __init__(self, arrayData, beginIndex,endIndex,arrayRes,indexR):
        self.arrayData = arrayData
        self.beginIndex = beginIndex
        self.endIndex = endIndex
        self.arrayRessult = arrayRes
        self.indexRes = indexR
    
    def workerExecute(parameterSum):
        sumArray = 0
        for i in range(parameterSum.beginIndex,parameterSum.endIndex):
            sumArray = sumArray + parameterSum.arrayData[i]
        parameterSum.arrayRessult[parameterSum.indexRes] = sumArray
        print(f'A soma do array: {parameterSum.arrayRessult[parameterSum.indexRes]}')
        return

#-----------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    sizeArray = 1000000 #Tamanho do array
    arrayA = empty(([sizeArray]))
    for i in range(len(arrayA)):
        arrayA[i] = i
    start_time = time.time()
    sum = 0.0
    for i in range(len(arrayA)):
        sum = sum + arrayA[i]
    end_time = time.time()
    print(arrayA)
    print(f'A soma dos elementos do array é: {sum}\nO tempo de processamento foi: {end_time-start_time}')
