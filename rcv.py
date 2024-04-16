import socket
import struct
from time import sleep
import sys 


# Crea un socket per la ricezione dei pacchetti
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
# Bind al dispositivo di rete
s.bind(("lo", 0))

# Dimensione massima dei dati da ricevere
BUFFER_SIZE =  1518

while True:
    # Ricevi il pacchetto
    packet, _ = s.recvfrom(BUFFER_SIZE)
    
    # Estrai i dati dal pacchetto
    ethernet_header = packet[:14]  # Ethernet header di 14 byte
    ip_header = packet[14:34]  # IP header di 20 byte
    data = packet[34:]  # Dati

    # Analizza l'header Ethernet per verificare se è il pacchetto desiderato
    destination_mac = ethernet_header[:6]
    source_mac = ethernet_header[6:12]
    protocol_type = ethernet_header[12:14]

    if protocol_type == b'\x08\x00':  # Protocollo IPv4
        # Analizza l'header IP
        version_ihl = ip_header[0]
        ttl = ip_header[8]
        protocol = ip_header[9]
        source_ip = socket.inet_ntoa(ip_header[12:16])
        destination_ip = socket.inet_ntoa(ip_header[16:20])

        # Decodifica i dati
        float_data = []
        for value in data.split(b','):
            if len(value) == 4:  # Assicura che ci siano 4 byte per il float
                float_data.append(struct.unpack('f', value)[0])
            else:
                #print("Errore: Dati non validi, la lunghezza non è di 4 byte.")
                pass

        # Stampa i dati ricevuti
        #print("Pacchetto ricevuto:")
        #print("Indirizzo IP di origine:", source_ip)
        #print("Indirizzo IP di destinazione:", destination_ip)
        if len(float_data)>0:
            print("Dati float:", float_data)
            print(len(float_data))
            dimensione_in_byte = sys.getsizeof(float_data)
            print(dimensione_in_byte)
            float_data.clear()
            sleep(5)

