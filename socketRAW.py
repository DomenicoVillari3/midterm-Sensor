import socket
import struct
from sensor_generate import generate_and_subsample
import sys

dati=generate_and_subsample(300,100)

l=[]
for dato in dati:
    l.append(dato[0])
    l.append(dato[1])
    l.append(dato[2])

print(len(l))




s=socket.socket(socket.AF_PACKET,socket.SOCK_RAW)
s.bind(("lo",0))


binary_data=b""


for f in dati:
    binary_data += struct.pack('f', f[0]) # asse x
    binary_data += b','# Aggiungi un delimitatore
    binary_data += struct.pack('f', f[1]) # asse y
    binary_data += b',' # Aggiungi un delimitatore
    binary_data += struct.pack('f', f[2]) # asse z
    binary_data += b',' # Aggiungi un delimitatore


# Rimuovi l'ultimo delimitatore
binary_data = binary_data[:-1]


header_ip=b"\x45\x00\00\x28"  #version, IHL, Type of service, Total Lenght
header_ip2=b"\xab\xcd\x00\x00" #Identification , Flags, Fragment Offset
header_ip3=b'\x40\x06\xa6\xec' #TTL, Protocol, Header Checksum
header_ip4=b'\x0a\x0a\x0a\x02' # Source address
header_ip5=b'\x0a\x0a\x0a\x01' #Destination address

header_ip=header_ip+header_ip2+header_ip3+header_ip4+header_ip5

MACdest=b'\x00\x0c\x29\xd3\xbe\xd6' #Mac address destination
MACsource=b'\x00\x0c\x29\xe0\xc4\xaf' #mac address source
ProtocolType=b'\x08\x00' #Protocol type (IPv4 )

header_Ethernet=MACdest+MACsource+ProtocolType


pkt=header_Ethernet +header_ip+binary_data


dimensione_in_byte = sys.getsizeof(dati)
print(dimensione_in_byte)
s.send(pkt)

