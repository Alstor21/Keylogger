import socket


# Define server host and port
HOST = '0.0.0.0'    # Listen on all interfaces, which includes localhost, lan, and wan
PORT = 65432        # non-privileged port (privileged ports are 1-1024)

# Create a socket object using IPv4 and TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))      # Bind the service to the address and port values
    server_socket.listen()                # Start listening for incoming connections
    print(f"Server listening on {HOST}:{PORT}")

    # Accept a client connection when requested
    connection, addr = server_socket.accept()
    with connection:
        print(f"Connected by {addr}")
        with open("recieved_log.txt", "wb") as recieved_file:
            while True:
                data = connection.recv(1024)    # Receive data from client
                if not data:
                    break                       # Exit loop if no data received
                revieved_file.write(data)       # Write received data to file
