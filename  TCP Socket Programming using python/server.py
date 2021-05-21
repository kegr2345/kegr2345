import os
import socket
import threading
import stat
import time
import datetime
#from tqdm import tqdm

IP = socket.gethostbyname(socket.gethostname())
PORT = 4473
ADDR = (IP,PORT)
SIZE = 1024
FORMAT = "utf-8"
SERVER_DATA_PATH = "server_data"
CLIENT_DATA_PATH = "client"

"""
CMD@Msg
"""

### to handle the clients
def handle_client (conn, addr):


    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send("OK@Welcome to the server.".encode(FORMAT))

    while True:
        data = conn.recv(SIZE).decode(FORMAT)
        data = data.split("@")
        cmd = data[0]
        
        
       
        

        if cmd == "LOGOUT":
            break

        elif cmd == "TASK":
            send_data = "OK@"
            send_data += "LOGOUT from the server.\n"
            send_data += "CREATING new file on the server.\n"
            send_data += "MULTITHREADING: handling multiple clients.\n"
            send_data += "UPLOAD <path>: Upload a file to the server.\n"
            send_data += "DOWNLOAD <filename>: Download a file from the server.\n"
            send_data += "DELETE <filename>: Delete a file from the server.\n"
            send_data += "DIR see content of shared folder.\n"

            conn.send(send_data.encode(FORMAT))
######
        elif cmd == "UPLOAD":
            
            name = data[1]
            text = data[2]
            #file_size = data[3]
            #bar = tqdm(range(file_size), f"Receiving {file_name}", unit="B", unit_scale=True, unit_divisor=SIZE)
            
            filepath = os.path.join(SERVER_DATA_PATH, name)
            with open(filepath, "w") as f:
                
                f.write(text)

            send_data = "OK@File uploaded to server."
            conn.send(send_data.encode(FORMAT))
            
        elif cmd == "DOWNLOAD":
            
            files = os.listdir(SERVER_DATA_PATH)
            path = data[1]
            print(data)
            name = path.split('/')[-1]
            send_data = "OK@"
            if name in files:
                
                with open(f"{path}", "r") as f:
                    text = f.read()
                print(text)

                #Im not sure how to get this to send the file and its contents to the client
                newFilePath = os.path.join(CLIENT_DATA_PATH, name)
                with open(newFilePath, "w") as f:
                    f.write(text)
                
                send_data += "File downloaded."
                
            else:
                send_data += "File not found."
            
            conn.send(send_data.encode(FORMAT))
        elif cmd == "DELETE":
            files = os.listdir(SERVER_DATA_PATH)
            send_data = "OK@"
            filename = data[1]

            if len(files) == 0:
                send_data += "The server directory is empty."
            else:
                if filename in files:
                    
                    os.system(f"rm {SERVER_DATA_PATH}/{filename}")
                    send_data += "File deleted."
                else:
                    send_data += "File not found."
            conn.send(send_data.encode(FORMAT))

        elif cmd == "DIR":
            files = os.listdir(SERVER_DATA_PATH)
            
            #i = 0
            send_data = "OK@"
            num_files = len(files)
           
            if num_files == 0:
                send_data += "Server directory is empty."
            else:
                send_data += "\n".join(f for f in files)
                #for i in files:
                    #newFilePath = os.path.join(CLIENT_DATA_PATH, files[i])
                    #fileStats = os.stat(newFilePath)
                    #timeMod = time.ctime(fileStats[stat.st_MTIME])
                    #file_size = so.
                    #send_data += files[i] + file_size
            
                    
            conn.send(send_data.encode(FORMAT))
######
        elif cmd == "CREATE":
            files = os.listdir(SERVER_DATA_PATH)
            fileName = data[1]


            if fileName in files: ##  condition if file already exist in the server.
                send_data += "File exist."
            else:
                buff = b"ABCD \n"
                with open(os.path.join(SERVER_DATA_PATH,fileName), 'wb') as temp_file: ##### creating the file
                    temp_file.write(buff)
                send_data += "File created"

            conn.send(send_data.encode(FORMAT))

    print(f"{addr} disconnected")
    conn.close()


def main():
    print("Starting the server")
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) ## used IPV4 and TCP connection
    server.bind(ADDR) # bind the address
    server.listen() ## start listening
    
    print(f"Server is listening on {IP}: {PORT}")
    
    

    while True:
        conn, addr = server.accept() ### accept a connection from a client
        thread = threading.Thread(target = handle_client, args = (conn, addr)) ## assigning a thread for each client

        thread.start()


if __name__ == "__main__":
    main()