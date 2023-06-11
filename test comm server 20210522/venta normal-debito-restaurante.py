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
		d1 = (
                         b'\x00\xC8\x60\x00\x00\x00\x06\x02\x10\x30\x38\x01\x00\x0E\xC0\x80'
                         b'\x06\x00\x00\x00\x00\x00\x00\x00\x10'
                     )

		trace = ClientData[25:29]

		d2 = (
                         b'\x12\x35\x55\x05\x19\x00\x10\x30\x37\x31\x34\x39\x30\x20\x20\x20'
                         b'\x20\x20\x20\x31\x32\x31\x37\x31\x33\x31\x31'
                      )
		
		terminal = ClientData[54:62]  

		d3 = (         
                         b'\x33\x33\x37\x35\x36\x34\x33\x34\x30\x20\x20\x20\x20'
                         b'\x20\x20\x06\x04\x00\x19\x00\x17\x30\x35\x39\x39\x30\x31\x34\x31'
                         b'\x33\x39\x30\x30\x34\x35\x37\x34\x38\x00\x98\x30\x31\x42\x46\x4C'
                         b'\x42\x42\x41\x4E\x43\x4F\x20\x46\x41\x4C\x41\x42\x45\x4C\x4C\x41'
                         b'\x20\x20\x20\x20\x20\x39\x35\x50\x30\x30\x30\x30\x30\x30\x30\x30'
                         b'\x30\x55\x73\x61\x20\x43\x4D\x52\x2F\x44\x65\x62\x69\x74\x6F\x20'
                         b'\x42\x46\x20\x64\x65\x73\x64\x65\x20\x53\x2F\x34\x39\x20\x79\x0A'
                         b'\x63\x61\x6E\x6A\x65\x61\x20\x70\x72\x6F\x6D\x6F\x20\x50\x69\x7A'
                         b'\x7A\x61\x20\x48\x75\x74\x20\x61\x20\x32\x36\x2E\x39'
                     ) 

		resp = d1 + trace + d2 + terminal + d3
		TCP_Client_Socket.send(resp)
		time.sleep(1)
		print ('Close client')
		TCP_Client_Socket.close()
	break

print ('Close Server')	
TCP_Server_Socket.close()
