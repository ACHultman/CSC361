from socket import *
import sys

def recv_msg(sock):
    # Read message length and unpack it into an integer
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    return recvall(sock, msglen)

def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data


try:
    clientSocket = socket(AF_INET, SOCK_STREAM)
except error as msg:
    print("Failed to create socket. Error code: " + str(msg[0]) + " , Error message : " + msg[1])
    sys.exit()
print("Socket Created")

host_ip = sys.argv[1]
host_port = int(sys.argv[2])
file_name = bytes(sys.argv[3], "utf-8")

clientSocket.connect((int(host_ip), host_port))
print("Socket Connected to " + host_ip + " on ip " + host_ip)

message = b"GET /" + file_name + b" HTTP/1.1\r\n\r\n"
clientSocket.sendall(message)
print("Message sent successfully")
'''
reply = clientSocket.recv(4096)
print(reply)
'''
reply = recv_msg(clientSocket)
print(reply)
