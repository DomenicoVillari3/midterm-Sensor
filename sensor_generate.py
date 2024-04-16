import numpy as np
from numpy.random import Generator, PCG64
from time import perf_counter, sleep

def generate_and_subsample(frequenza_campionamento_originale, frequenza_campionamento_desiderata):
    start_time = perf_counter()
    rg = Generator(PCG64())
    durata_segnale = 1  # Secondi
    numero_campioni_originale = int(frequenza_campionamento_originale * durata_segnale)

    # Generazione di segnali casuali (600 valori per ogni segnale)
    segnale1 = rg.uniform(-5, 5, numero_campioni_originale)
    segnale2 = rg.uniform(-5, 5, numero_campioni_originale)
    segnale3 = rg.uniform(-5, 5, numero_campioni_originale)

    # Determinazione del fattore di downsampling
    fattore_downsampling = int(frequenza_campionamento_originale / frequenza_campionamento_desiderata)

    '''Calcolo della media dei campioni consecutivi
        Il motivo per cui facciamo il reshape è per far si che la media venga fatta per valori a 3 a 3 (Nel nostro caso)
        Infatti, l'array per ogni segnale è unidimensionale, facciamo un esempio con frequenza 9 e sumsampling a 3, in modo da ottenere 3
        come fattore di downsampling:
        [-0.14074699  1.56239642 -0.06591029 -0.71355907 -0.68971163 -0.12130035 -0.61073159  0.82995997 -1.15069117].
        Nel momento in cui facciamo il reshape trasformiamo l'array in:
        [[-0.14074699  1.56239642 -0.06591029]
        [-0.71355907 -0.68971163 -0.12130035]
        [-0.61073159  0.82995997 -1.15069117]]
        Come possiamo vedere i dati sono organizzati in sottoarray con tre elementi. In questo modo la funzione np.mean() andrà a fare la media 
        dei sottoarray (axis=1 vuol dire lungo le colonne, nel nostro caso solo una colonna).
        Quindi [-0.14074699  1.56239642 -0.06591029] sarà la somma divisa per 3, che fa 0.45191305 e così via per gli altri elementi (colonne).
        Alla fine avremo un array unidimensionale:  [ 0.45191305 -0.50819035 -0.3104876 ] che verrà inserito nella sottolista e infine nella macrolista.
    '''
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

    sleep(1 - generation_time)
    
    return macrolista_subsamp

    # PER MIMMO: quando importi questa funzione, ricordati che ritorna una tupla: il primo valore è la lista di valori
    # subsamplati, il secondo è il tempo che ci è stato a generarli (usalo per sistemare la frequenza)

lista_sub = generate_and_subsample(600, 200)
print(lista_sub)

