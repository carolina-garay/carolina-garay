import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
from numpy import linalg as LA

#---------------Funciones-----------------

def masa(A):
    #Pasaje de momentos de cada particula a un vector y energia total
    masa=[]
    N = A.shape[0]
    for i in range(N):
        PParticula1 = np.array(A.iloc[i,1:4])
        PParticula2 = np.array(A.iloc[i,5:8])
        PParticula3 = np.array(A.iloc[i,9:12])
        PParticula4 = np.array(A.iloc[i,13:16])
        PTotal = PParticula1+PParticula2+PParticula3+PParticula4
        ETotal = A.iloc[i,0] + A.iloc[i,4] + A.iloc[i,8] + A.iloc[i,12]
        ModuloPTotal = LA.norm(PTotal)
        masasub = ((ETotal)**2-(ModuloPTotal)**2)**(1/2)
        masa.append(masasub)
    return(masa)

def Histogramadatos(A):
    H = []
    N = len(A)
    for i in range (N):
        Bandera = False
        j = 1
        while not Bandera:    
            if A[i] <= 5*j:
                Bandera = True
                H.append(j)
            else:
                j +=1
    return(H)
                
#------------Programa principal-------------
MasasInvariantes2 = []
MasasInvariantes3 = []
MasasInvariantes4 = []
MasasInvariantes5 = []
RangoMasas1 = []
RangoMasas2 = []
RangoMasas3 = []
RangoMasas4 = []
RangoMasas5 = []
#Cargando los archivos csv a python
DeDmu2011_raw = pd.read_csv("2e2mu_2011.csv")
DeDmu2012_raw = pd.read_csv("2e2mu_2012.csv")
Ce2011_raw = pd.read_csv("4e_2011.csv")
Ce2012_raw = pd.read_csv("4e_2012.csv")
Cmu2011_raw = pd.read_csv("4mu_2011.csv")

#----------------------------------------------

#Filtrado de las variables que vamos a utilizar. Los numeros son identificadores para las masas
#1
DeDmu2011 = DeDmu2011_raw[["E1","px1","py1","pz1","E2","px2","py2","pz2","E3","px3","py3","pz3","E4","px4","py4","pz4"]]
#2
DeDmu2012 = DeDmu2012_raw[["E1","px1","py1","pz1","E2","px2","py2","pz2","E3","px3","py3","pz3","E4","px4","py4","pz4"]]
#3
Ce2011 = Ce2011_raw[["E1","px1","py1","pz1","E2","px2","py2","pz2","E3","px3","py3","pz3","E4","px4","py4","pz4"]]
#4
Ce2012 = Ce2012_raw[["E1","px1","py1","pz1","E2","px2","py2","pz2","E3","px3","py3","pz3","E4","px4","py4","pz4"]]
#5
Cmu2011 = Cmu2011_raw[["E1","px1","py1","pz1","E2","px2","py2","pz2","E3","px3","py3","pz3","E4","px4","py4","pz4"]]

#---------------------------------------------

#Llamados a la subfuncion para el calculo de las masas invariantes
MasasInvariantes1 = masa(DeDmu2011)
MasasInvariantes2 = masa(DeDmu2012)
MasasInvariantes3 = masa(Ce2011)
MasasInvariantes4 = masa(Ce2012)
MasasInvariantes5 = masa(Cmu2011)

#----------------plot-----------------
#Rangos
RangoMasas1 = Histogramadatos(MasasInvariantes1)
RangoMasas2 = Histogramadatos(MasasInvariantes2)
RangoMasas3 = Histogramadatos(MasasInvariantes3)
RangoMasas4 = Histogramadatos(MasasInvariantes4)
RangoMasas5 = Histogramadatos(MasasInvariantes5)

#Concatenacion
RangoMasas = []
RangoMasas.extend(RangoMasas1)
RangoMasas.extend(RangoMasas2)
RangoMasas.extend(RangoMasas3)
RangoMasas.extend(RangoMasas4)
RangoMasas.extend(RangoMasas5)

Contador = []
Yaxis = []
for j in range(max(RangoMasas)):
    Yaxis.append(j*5)
    cont = 0
    for i in range(len(RangoMasas)):
        if RangoMasas[i] == j: cont += 1
    Contador.append(cont)
    
#Ploteado en si
plot.bar(Yaxis, Contador, color="c",width=10)
plot.style.use("fivethirtyeight")
plot.xlabel("Masa de los 4 leptones (GeV/c²)")
plot.ylabel("Número de colisiones")
plot.title("Histograma de masas de 4 leptones en colision protón-protón")
plot.grid(True)
plot.show()