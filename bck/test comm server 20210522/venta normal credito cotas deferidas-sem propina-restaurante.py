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
                         b'\x00\xD8\x60\x00\x00\x00\x06\x02\x10\x30\x38\x01\x00\x0E\xC1\x80' 
                         b'\x06\x00\x00\x00\x00\x00\x00\x00\x01'
                     )

		trace = ClientData[25:29]

		d2 = (
                         b'\x15\x04\x19\x05\x20\x00\x10\x30\x37\x31\x36\x31\x34\x20\x20\x20'
                         b'\x20\x20\x20\x31\x34\x34\x35\x33\x35\x31\x31' 
                      )
		
		terminal = ClientData[54:62]  

		d3 = (         
                         b'\x33\x33\x37\x35\x36\x34\x33\x34\x30\x20\x20\x20\x20' 
                         b'\x20\x20\x00\x22\x30'
                     )    

		cotas = ClientData[80:82]         

		d4 = (
                         b'\x30\x30\x30\x30\x30\x30\x30\x30\x30' 
                         b'\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x06\x04\x00\x19\x00\x17' 
                         b'\x30\x35\x39\x39\x30\x31\x34\x31\x34\x30\x30\x30\x34\x35\x38\x31' 
                         b'\x34\x00\x90\x30\x31\x43\x45\x4E\x43\x43\x45\x4E\x43\x4F\x53\x55' 
                         b'\x44\x20\x50\x45\x52\x55\x20\x20\x20\x20\x20\x20\x20\x38\x35\x50' 
                         b'\x30\x30\x30\x30\x30\x30\x30\x30\x30\x45\x6E\x20\x65\x73\x74\x65' 
                         b'\x20\x63\x6F\x6D\x65\x72\x63\x69\x6F\x20\x6E\x6F\x20\x73\x65\x20' 
                         b'\x65\x78\x69\x67\x65\x0A\x6D\x6F\x6E\x74\x6F\x20\x6D\x69\x6E\x69' 
                         b'\x6D\x6F\x20\x64\x65\x20\x63\x6F\x6D\x70\x72\x61\x0A'
                     ) 

		resp = d1 + trace + d2 + terminal + d3 + cotas + d4
		TCP_Client_Socket.send(resp)
		time.sleep(1)
		print ('Close client')
		TCP_Client_Socket.close()
	break

print ('Close Server')	
TCP_Server_Socket.close()
