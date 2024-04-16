from threading import Thread
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import Generator, PCG64
from time import perf_counter
import time
from itertools import count

from sensor_generate import generate_and_subsample


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
    #subplot per avere una finestra con 3 grafici differenti 
    fig, axs = plt.subplots(3, 1, figsize=(8, 12))
    
    #liste per conetere i dati da plottare 
    index=0
    indexes=[]
    x_vals=[]
    y_vals=[]
    z_vals=[]


    for element in lista:
        #appendo i punti alla lista corrispondente
        indexes.append(index)
        x_vals.append(element[0])
        y_vals.append(element[1])
        z_vals.append(element[2])
        index+=1

        #faccio i 3 plot 
        axs[0].plot(indexes,x_vals,'b-')
        axs[1].plot(indexes,y_vals,'g-')
        axs[2].plot(indexes,z_vals,'r-')
        axs[0].set_xlabel('X')  # Etichetta per l'asse y del primo grafico
        axs[1].set_xlabel('Y')  # Etichetta per l'asse y del secondo grafico
        axs[2].set_xlabel('Z')  # Etichetta per l'asse y del terzo grafico
        
        #uso plt pause per rallentare la generazione del plt
        if index%10==0:
            plt.pause(0.1) 
        
        #rimuovo i dati precedenti ogni 200 valori
        if index %200==0:
            print("clear")
            x_vals=x_vals[200:]
            y_vals=y_vals[200:]
            z_vals=z_vals[200:]
            indexes=indexes[200:]
            #mi assicuro che alla fine non venga pulito il plot 
            if index %600 !=0:
                axs[0].cla()
                axs[1].cla()
                axs[2].cla()
                plt.cla()
            

        

    plt.show()




    plt.ioff()
    plt.show()

if __name__ == '__main__':
    main()
