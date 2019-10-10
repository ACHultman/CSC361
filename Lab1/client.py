from socket import *
import sys

try:
    clientSocket = socket(AF_INET, SOCK_STREAM)
except error as msg:
    print("Failed to create socket. Error code: " + str(msg[0]) + " , Error message : " + msg[1])
    sys.exit()
print("Socket Created")

host_ip = sys.argv[1]
host_port = int(sys.argv[2])
file_name = bytes(sys.argv[3], "utf-8")

clientSocket.connect((host_ip, host_port))
print("Socket Connected to " + host_ip + " on ip " + host_ip)

message = b"GET /" + file_name + b" HTTP/1.1\r\n\r\n"
clientSocket.sendall(message)
print("Message sent successfully")

fragments = []
while True: 
    chunk = clientSocket.recv(10000)
    if not chunk: 
        break
    fragments.append(chunk)

reply = b''.join(fragments)
print(reply)