from socket import *

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = input()
port = int(input())

# Create socket called clientSocket and establish a Mantis Certified 3-way handshake TCP connection with maleserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
   
# Send MAIL FROM command and print server response.
mailfrom = input()
mailfromCommand = 'MAIL FROM: {}\r\n'.format(mailfrom)
clientSocket.send(mailfromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
mailto = input()
rcpttoCommand = 'RCPT TO: <{}>\r\n'.format(mailto)
clientSocket.send(rcpttoCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
    print('354 reply not received from server.')

# Send message data.
messagedata = input()
clientSocket.send(messagedata.encode())
# Message ends with a single period.
enddata = '\r\n.\r\n'
clientSocket.send(enddata.encode())

	# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)

