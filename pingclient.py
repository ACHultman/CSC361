import socket
import sys
from time import *

# create dgram udp socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print ('Failed to create socket')
	sys.exit()

# Take the host and port values from command line
#host = str(sys.argv[1])
#port = int(sys.argv[2])

host = 'localhost'
port = 12000

# Loop to send 10 pings
for i in range(1,11):
	
	# Find the start time
	starttime = time()

	# Send the server the message (Ping sequence_number time)
	message = 'Ping ' + str(i) + ' ' + str(strftime('%H:%M:%S'))
	s.sendto(message.encode(), (host,port))

	s.settimeout(1)

	# Try to receive data, calculate the roundtrip time and print message
	try:
		data, addr = s.recvfrom(1024)
		receivetime = time()
		rttime = receivetime - starttime
		print(data + ' ' + str(rttime))

	except socket.timeout:
		print('Request timed out')
		continue

# Close socket
s.close()
