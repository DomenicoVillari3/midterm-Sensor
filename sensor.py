from threading import Thread
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import Generator, PCG64
from time import perf_counter
import time
from itertools import count

from sensor_generate import generate_and_subsample
from csv_writer import write_to_csv  # Importa la funzione per scrivere i dati nel file CSV

freq_inziale= 600 # 0.6 kHz
freq_desiderata= 200 # 0.2 kHz



def main():
    lista = generate_and_subsample(freq_inziale, freq_desiderata)
    write_to_csv(lista, 'dati_generati.csv')  # Scrive i dati nel file CSV
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
        if index %(freq_desiderata//2)==0:
            x_vals=x_vals[(freq_desiderata//2):]
            y_vals=y_vals[(freq_desiderata//2):]
            z_vals=z_vals[(freq_desiderata//2):]
            indexes=indexes[(freq_desiderata//2):]
            #mi assicuro che alla fine non venga pulito il plot 
            if index %freq_desiderata !=0:
                axs[0].cla()
                axs[1].cla()
                axs[2].cla()
                plt.cla()
            
    plt.show()





if __name__ == '__main__':
    main()
