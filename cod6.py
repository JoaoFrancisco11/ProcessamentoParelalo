# Objetivo: Comparar o tempo de processamento de um código sequencial e um código com processamento paralelo
# 
# Fluxo do código: Será construído um array com 1000000 elementos e será feita a soma de todos os elementos
# do array através de processamento sequencial e processamento paralelo.
# Através do código sequencial, o objetivo é fazer a soma dos números um a um.
# Com o processamento paralelo, o objetivo é dividir o array em partes iguais e ir somando os números que
# estão divididos em cada parte paralelamente.

#----------------------------------------------------------------------------------------------------------------
# A classe Process é utilizada para fazer o processamento paralelo
# Para criar o array importamos o módulo empty
# E, por fim, usaremos a biblioteca time para calcular o tempo de processamento. 
from multiprocessing import Process
import multiprocessing 
from numpy import empty
import time

from pandas import array

# ----------------------------------------------------------------------------------------------------------------
# Cria-se uma classe para fazer o processamento paralelo
class ParameterSum():   
    def __init__(self, arrayData, beginIndex,endIndex,arrayRes,indexR):
        # definindo os atributos
        self.arrayData = arrayData
        self.beginIndex = beginIndex
        self.endIndex = endIndex
        self.arrayRessult = arrayRes
        self.indexRes = indexR
        
    # definindo os métodos
    def _workerExecute(parameterSum):
        """
        Parâmetros
        ----------
        parameterSum: array
            Nesse caso, o array é formado por números inteiros.
        """
        sumArray = 0
        for i in range(parameterSum.beginIndex,parameterSum.endIndex):
            sumArray = sumArray + parameterSum.arrayData[i]
        parameterSum.arrayRessult[parameterSum.indexRes] = sumArray
        print(f'A soma do array: {parameterSum.arrayRessult[parameterSum.indexRes]}')
        return

#-----------------------------------------------------------------------------------------------------------------
# main
if __name__ == "__main__":
    sizeArray = 1000000 #Tamanho do array
    arrayA = empty(([sizeArray]))   # criando um array  
    for i in range(len(arrayA)):
        arrayA[i] = i   #colocando valores no array
    #   Início do Processamento sequencial
    start_time = time.time()
    sum = 0.0
    for i in range(len(arrayA)):
        sum = sum + arrayA[i]   #Soma dos elementos do array
    end_time = time.time()
    #   Término do processamento sequencial
    print("A soma dos elementos do array é: %f\nTempo de Processamento: %f" %(sum, (end_time - start_time)))
    
    # Início do Processamento Paralelo
    start_time = time.time()
    arrayRes = multiprocessing.Array('d', 4) # alocando um espaço da memória que será usado e acessado pelas funções
    for i in range(len(arrayRes)):
        arrayRes = 0.0
        #------- Aqui é feita a quebra do array
        dim1 = 0
        dim2 = int(len(arrayA)/4)
        dim3 = int(2*dim2)
        dim4 = int(3*dim2)
        dim5 = int(len(arrayA))
        #---------
        parameterSum1 = ParameterSum(arrayA,dim1,dim2,arrayRes,0) 
