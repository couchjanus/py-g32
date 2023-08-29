# 
import socket

srv = socket.socket()

# print(dir(srv))

print(srv.fileno())
print(srv.proto)
srv.close()