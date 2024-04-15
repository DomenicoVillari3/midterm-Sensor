import numpy as np
from numpy.random import Generator, PCG64
from time import perf_counter

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


