import socket
import struct
from tmp_file.sensor_generate import generate_and_subsample
import sys

dati=generate_and_subsample(600,200)

l=[]
for dato in dati:
    l.append(dato[0])
    l.append(dato[1])
    l.append(dato[2])

print(len(l))


host="127.0.0.1"
port=65435

binary_data=b""


for f in dati:
    binary_data += struct.pack('f', f[0]) # asse x
    #binary_data += b','# Aggiungi un delimitatore
    binary_data += struct.pack('f', f[1]) # asse y
    #binary_data += b',' # Aggiungi un delimitatore
    binary_data += struct.pack('f', f[2]) # asse z
    #binary_data += b',' # Aggiungi un delimitatore


# Rimuovi l'ultimo delimitatore
#binary_data = binary_data[:-1]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(binary_data)
            #s.send(b"")
            s.close()
