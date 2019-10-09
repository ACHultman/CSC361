from socket import *
import sys

try:
    clientSocket = socket(AF_INET, SOCK_STREAM)
except error as msg:
    print("Failed to create socket. Error code: " + str(msg[0]) + " , Error message : " + msg[1])
    sys.exit()
print("Socket Created")

host_ip = sys.argv[1]
host_port = sys.argv[2]
file = sys.argv[3]

clientSocket.connect((int(host_ip), host_port))
print("Socket Connected to " + host_ip + " on ip " + host_ip)

message = "GET /" + file + " HTTP/1.1\r\n\r\n"
clientSocket.sendall(message)
print("Message sent successfully")
reply = clientSocket.recv(4096)
print(reply)
