import socket
import struct
import sys
from time import sleep

def main():
    server_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    server_socket.bind(("lo",0))  
    print("Server ready, waiting for client...")
    sleep(2)
    while True:
        packet, addr = server_socket.recvfrom(2434)
        
        # Estrai i dati dal pacchetto
        ethernet_header = packet[:14]  # Ethernet header di 14 byte
        ip_header = packet[14:34]  # IP header di 20 byte
        data = packet[34:]  # Dati
        # Analizza l'header Ethernet per verificare se è il pacchetto desiderato
        destination_mac = ethernet_header[:6]
        source_mac = ethernet_header[6:12]
        protocol_type = ethernet_header[12:14]
        
        if  protocol_type == b'\x08\x00' :
            if len(data)%4!=0:
                continue
            float_data =[]
            for i in range(0,len(data),4):
                if(i+4 <= len(data)):
                    unpacked_data = struct.unpack('f' ,data[i:i+4])
                else:
                    unpacked_data = struct.unpack('f' ,data[i:len(data)])
                
                float_data.append(unpacked_data)
            
            print("Data received: ", float_data)
            print("len: ", len(float_data))
            
        dimensione_in_byte = sys.getsizeof(packet)
        print("dim PKT: ",dimensione_in_byte)
        if len(float_data)==300:
            break
        

if __name__ == "__main__":
    main()