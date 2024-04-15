import numpy as np
from numpy.random import Generator, PCG64
from time import perf_counter, sleep

def generate_and_subsample(frequenza_campionamento_originale, frequenza_campionamento_desiderata, time_to_wait):
    start_time = perf_counter()
    wait_time = 1 - time_to_wait
    sleep(wait_time)
    rg = Generator(PCG64())
    durata_segnale = 1  # Secondi
    numero_campioni_originale = int(frequenza_campionamento_originale * durata_segnale)

    # Generazione di segnali casuali (600 valori per ogni segnale)
    segnale1 = rg.standard_normal(numero_campioni_originale)
    segnale2 = rg.standard_normal(numero_campioni_originale)
    segnale3 = rg.standard_normal(numero_campioni_originale)

    # Determinazione del fattore di downsampling
    fattore_downsampling = int(frequenza_campionamento_originale / frequenza_campionamento_desiderata)

    # Calcolo della media dei campioni consecutivi
    segnale1_subsamp = np.mean(segnale1.reshape(-1, fattore_downsampling), axis=1)
    segnale2_subsamp = np.mean(segnale2.reshape(-1, fattore_downsampling), axis=1)
    segnale3_subsamp = np.mean(segnale3.reshape(-1, fattore_downsampling), axis=1)

    # Creazione della macrolista sottocampionata mantenendo la struttura di liste
    macrolista_subsamp = []

    for i in range(len(segnale1_subsamp)):
        sottolista = [segnale1_subsamp[i], segnale2_subsamp[i], segnale3_subsamp[i]]
        macrolista_subsamp.append(sottolista)

    end_time = perf_counter()

    generation_time = end_time - start_time

    return macrolista_subsamp, generation_time

    # PER MIMMO: quando importi questa funzione, ricoradati che ritorna una tupla: il primo valore è la lista di valori
    # subsamplati, il secondo è il tempo che ci è stato a generarli (usalo per sistemare la frequenza)
lista_sub, end_time = generate_and_subsample(30, 10, 0)

print(lista_sub)
