# 
import socket

HOST = '127.0.0.1'
PORT = 65432

with  socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Started ech server on {HOST}:{PORT}")
    
    try:
        conn, addr = s.accept()
        with conn:
            print(F"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                print(f"Recived {data} from {addr}")
                if not data:
                    print(f"Breaking connection for {addr}")
                    break
                conn.sendall(data)
                print(f"Sended {data} to {addr}")
    except KeyboardInterrupt:
        print(f"\KeyboardInterrupt exception. Exiting.\n")
            
                
    
