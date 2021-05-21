import os
import socket


IP = "localhost"
PORT = 4450
ADDR = (IP,PORT)
SIZE = 1024
FORMAT = "utf-8"
SERVER_DATA_PATH = "server_data"

def main():
    
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ADDR)
    while True:
        data = client.recv(SIZE).decode(FORMAT)
        cmd, msg = data.split("@")
        if cmd == "OK":
            print(f"{msg}")
        elif cmd == "DISCONNECTED":
            print(f"{msg}")
            break
        
        data = input("> ") 
        data = data.split(" ")
        cmd = data[0]

        if cmd == "HELP":
            client.send(cmd.encode(FORMAT))
        elif cmd == "LOGOUT":
            client.send(cmd.encode(FORMAT))
            break
        elif cmd == "UPLOAD":
            path = data[1]
            with open(f"{path}", "r") as f:
                text = f.read()

            filename = path.split("/")[-1]
            send_data = f"{cmd}@{filename}@{text}"
            client.send(send_data.encode(FORMAT))

        elif cmd == "DOWNLOAD":
            path = data[1]
            print(data)
            filename = path.split('/')[-1]
            
            filepath = os.path.join(SERVER_DATA_PATH, filename)
            print(filepath)

            send_data = f"{cmd}@{path}"
            client.send(send_data.encode(FORMAT))
            
        elif cmd == "DELETE":
            client.send(f"{cmd}@{data[1]}".encode(FORMAT))


    print("Disconnected from the server.")
    client.close() ## close the connection

if __name__ == "__main__":
    main()