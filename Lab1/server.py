from socket import *
import sys  # In order to terminate the program

HOST = '10.0.0.1'
PORT = 1234
print("Server host: " + HOST)


# Preparing server socket:

try:
    serverSocket = socket(AF_INET, SOCK_STREAM)
except error as msg:
    print("Failed to create socket. Error code: " + str(msg[0]) + " , Error message: " + msg[1])
    sys.exit()
print("Server TCP Socket Created")

try:
    serverSocket.bind((HOST, PORT))
except error as msg:
    print("Bind failed. Error Message: " + str(msg))
    sys.exit()
print("Socket bind complete to port " + str(PORT))

serverSocket.listen(10)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print("Connected with " + addr[0] + ":" + str(addr[1]))
    try:
        message = connectionSocket.recv(1024)
        print(message.split()[1].decode("utf-8"))
        filename = message.split()[1].decode("utf-8")
        f = open(filename[1:])

        outputdata = f.read()
        # Send one HTTP header line into socket
        connectionSocket.send(('HTTP/1.1 200 OK\n' + 'Content-Type: text/html\n' + '\r\n').encode("utf-8"))
        print("sent header")
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
		
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n')
        # Close client socket
        connectionSocket.close()
