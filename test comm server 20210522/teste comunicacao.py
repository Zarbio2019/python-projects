import socket
import time

Hostname = '192.168.6.9'
PortNumber = 15000
Buffer = 500
ServerAddress = (Hostname, PortNumber)

TCP_Server_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP_Server_Socket.bind(ServerAddress)
TCP_Server_Socket.listen(2)

while 1:
	print ('Server is waiting for connection')
	TCP_Client_Socket, ClientAddress = TCP_Server_Socket.accept()
	print ('Server has accepted the connection request from ',ClientAddress)
	
	print ('The Server is ready to receive data from the client')
	ClientData = TCP_Client_Socket.recv(Buffer)
	if ClientData:
		print ('The POS has sent this data string: ', ClientData)
		TCP_Client_Socket.send(b'\x00\x23\x60\x00\x00\x00\x06\x08'
                                       b'\x10\x20\x18\x01\x00\x02\x80\x00'
                                       b'\x00\x99\x00\x00\x11\x09\x03\x10'
                                       b'\x18\x08\x00\x30\x30\x33\x33\x37'
                                       b'\x30\x30\x30\x00\x00')
		time.sleep(1)
		print ('Close client')
		TCP_Client_Socket.close()
	break

print ('Close Server')	
TCP_Server_Socket.close()
