import socket


Target_host = "127.0.0.1"
Target_port = 9997

#create a socket object
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


#send some data
client.sendto(b"AAABBBBCCCKSDSSJ",(Target_host,Target_port))


#recieve some data
data, addr = client.recvfrom(4096)


print(data.decode())
client.close()