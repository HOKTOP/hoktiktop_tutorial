import os 
import socket

HOST = "192.168.1.2"
PORT = 8484

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ss:
    ss.bind((HOST,PORT))
    ss.listen()
    conn ,ipinfo = ss.accept()
    while(conn):
        print(f"connected by :{ipinfo}")
        message= conn.recv(1024)
        while True:
            print(f"message:{message.decode()}")
            message= conn.recv(1024)
            if(message.decode() == "0/"):
                os.system("shutdown -s -t 1") 
