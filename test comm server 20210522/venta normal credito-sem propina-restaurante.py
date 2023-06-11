import socket
import time

Hostname = '10.119.67.10'
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
                         b'\x11\x26\x14\x05\x20\x00\x10\x30\x37\x31\x35\x30\x33\x20\x20\x20'
                         b'\x20\x20\x20\x31\x31\x30\x37\x33\x30\x31\x31'
                      )
		
		terminal = ClientData[54:62]  

		d3 = (         
                         b'\x33\x33\x37\x35\x36\x34\x33\x34\x30\x20\x20\x20\x20' 
                         b'\x20\x20\x06\x04\x00\x19\x00\x17\x30\x35\x39\x39\x30\x31\x34\x31' 
                         b'\x34\x30\x30\x30\x34\x35\x37\x35\x35\x00\x98\x30\x31\x43\x45\x4E' 
                         b'\x43\x43\x45\x4E\x43\x4F\x53\x55\x44\x20\x50\x45\x52\x55\x20\x20' 
                         b'\x20\x20\x20\x20\x20\x38\x38\x50\x30\x30\x30\x30\x30\x30\x30\x30' 
                         b'\x30\x4E\x6F\x20\x63\x6F\x6D\x70\x61\x72\x74\x61\x73\x20\x74\x75' 
                         b'\x20\x69\x6E\x66\x2E\x20\x73\x65\x6E\x73\x69\x62\x6C\x65\x0A\x28' 
                         b'\x63\x6C\x61\x76\x65\x73\x2C\x20\x63\x75\x65\x6E\x74\x61\x73\x2C' 
                         b'\x20\x23\x20\x74\x61\x72\x6A\x65\x74\x61\x73\x29\x0A'
                     ) 

		resp = d1 + trace + d2 + terminal + d3
		TCP_Client_Socket.send(resp)
		time.sleep(1)
		print ('Close client')
		TCP_Client_Socket.close()
	break

print ('Close Server')	
TCP_Server_Socket.close()
