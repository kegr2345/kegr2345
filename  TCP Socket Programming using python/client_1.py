import os
import socket
#from tqdm import tqdm #This is to make a progress bar.


IP = socket.gethostbyname(socket.gethostname())
PORT = 4473
ADDR = (IP,PORT)
SIZE = 1024 ## byte .. buffer size
FORMAT = "utf-8"
SERVER_DATA_PATH = "server_data"
CLIENT_DATA_PATH = "client"

def main():
    print('Type "CONNECT" to connect to the server.')
    command = input("> ")
    while command != "CONNECT":
        print("You were not connected.")
        print('Type "CONNECT" to connect to the server.')
        command = input("> ")
        
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ADDR)

    while True:  ### multiple communications
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
        
        
            

        if cmd == "TASK":
            client.send(cmd.encode(FORMAT))

        elif cmd == "UPLOAD":
            
            path = data[1]
            
            
            #file_size = os.path.data(file_name)   #why the hell isnt this working
            
            #bar = tqdm(range(file_size), f"sending{file_name}", unit="B", unit_scale=True, unit_divisor=SIZE)
            with open(f"{path}", "r") as f:
                
                    
                text = f.read()
                    
                    
                    #bar.update(len(file_data))

            file_name = path.split('/')[-1]
            send_data = f"{cmd}@{file_name}@{text}"
            client.send(send_data.encode(FORMAT))

        elif cmd == "DOWNLOAD":
            path = data[1]
            print(data)
            filename = path.split('/')[-1]
            
            filepath = os.path.join(SERVER_DATA_PATH, filename)
            print(filepath)#this is just to check my work.

            send_data = f"{cmd}@{path}"
            client.send(send_data.encode(FORMAT))
        elif cmd == "DELETE":
            client.send(f"{cmd}@{data[1]}".encode(FORMAT))

        elif cmd == "DIR":
            client.send(cmd.encode(FORMAT))

        elif cmd == "LOGOUT":
            client.send(cmd.encode(FORMAT))
            break
      
        elif cmd == "CREATE":
            print(f"{cmd}@{data[1]}")       ### two words are separated by @ character.
            client.send(f"{cmd}@{data[1]}".encode(FORMAT))


    print("Disconnected from the server.")
    client.close() ## close the connection

if __name__ == "__main__":
    main()