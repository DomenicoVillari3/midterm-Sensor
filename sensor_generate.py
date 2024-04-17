import numpy as np
from numpy.random import Generator, PCG64
from time import perf_counter, sleep
import csv

def generate_and_subsample(frequenza_campionamento_originale, frequenza_campionamento_desiderata, output_file):

    start_time = perf_counter()
    rg = Generator(PCG64()) # classe per generare numeri casuali e pcg64 è l'algoritmo usato
    numero_campioni_originale = int(frequenza_campionamento_originale)

    # Generazione di segnali casuali (600 valori per ogni segnale) compresi tra -5 e 5
    segnale1 = rg.uniform(-5, 5, numero_campioni_originale)
    segnale2 = rg.uniform(-5, 5, numero_campioni_originale)
    segnale3 = rg.uniform(-5, 5, numero_campioni_originale)

    # Determinazione del fattore di downsampling 
    fattore_downsampling = int(frequenza_campionamento_originale / frequenza_campionamento_desiderata)

    segnale1 = np.float32(segnale1)
    segnale2 = np.float32(segnale2)
    segnale3 = np.float32(segnale3)

    segnale1_subsamp = np.mean(segnale1.reshape(-1, fattore_downsampling), axis=1)
    segnale2_subsamp = np.mean(segnale2.reshape(-1, fattore_downsampling), axis=1)
    segnale3_subsamp = np.mean(segnale3.reshape(-1, fattore_downsampling), axis=1)

    # Creazione della macrolista sottocampionata mantenendo la struttura di liste
    macrolista_subsamp = []

    for i in range(len(segnale1_subsamp)):
        sottolista = [segnale1_subsamp[i], segnale2_subsamp[i], segnale3_subsamp[i]]
        macrolista_subsamp.append(sottolista)

    # Scrittura dei valori su un file CSV
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['x', 'y', 'z'])  # Intestazione delle colonne nel file CSV
        for sublist in macrolista_subsamp:
            writer.writerow(sublist)  # Scrivi ogni sottolista come una riga nel file CSV

    end_time = perf_counter()

    generation_time = end_time - start_time

    sleep(1 - generation_time)  # Assicura che il tempo totale sia almeno 1 secondo
    return macrolista_subsamp, generation_time

# Esempio di utilizzo:
output_file = "output.csv"
lista_sub, tempo_generazione = generate_and_subsample(600, 200, output_file)
print(f"I valori sono stati scritti nel file '{output_file}'. Tempo di generazione: {tempo_generazione} secondi.")
