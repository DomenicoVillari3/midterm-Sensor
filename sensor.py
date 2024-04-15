from threading import Thread
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import Generator, PCG64
from time import perf_counter
import time
from itertools import count


def generate():
    start = perf_counter()
    rg = Generator(PCG64())

    # Parametri del segnale
    frequenza_campionamento = 600  # Campioni al secondo
    durata_segnale = 1  # Secondi
    numero_campioni = int(frequenza_campionamento * durata_segnale)

    # Generazione di segnali casuali (600 valori per ogni segnale)
    segnale1 = rg.standard_normal(numero_campioni)
    segnale2 = rg.standard_normal(numero_campioni)
    segnale3 = rg.standard_normal(numero_campioni)

    # Creazione della macrolista
    macrolista = []

    # Creazione di sottoliste con 3 segnali ciascuna
    for i in range(numero_campioni):
        sottolista = [segnale1[i], segnale2[i], segnale3[i]]
        macrolista.append(sottolista)

    # Stampa della macrolista
    end = perf_counter()

    print(macrolista)
    print(end-start)
    return macrolista



def main():
    lista=generate()
    myplot(lista=lista)



def myplot(lista):
    fig, axs = plt.subplots(3, 1, figsize=(8, 12))
    
    #liste per conetere i dati da plottare 
    index=count()
    indexes=[]
    x_vals=[]
    y_vals=[]
    z_vals=[]

    

    for element in lista:
        indexes.append(next(index))
        x_vals.append(element[0])
        y_vals.append(element[1])
        z_vals.append(element[2])

        axs[0].plot(indexes,x_vals,'b-')
        axs[1].plot(indexes,y_vals,'g-')
        axs[2].plot(indexes,z_vals,'r-')
        axs[0].set_xlabel('X')  # Etichetta per l'asse y del primo grafico
        axs[1].set_xlabel('Y')  # Etichetta per l'asse y del secondo grafico
        axs[2].set_xlabel('Z')  # Etichetta per l'asse y del terzo grafico
        plt.pause(0.01) 

        

    plt.show()




    plt.ioff()
    plt.show()

if __name__ == '__main__':
    main()
