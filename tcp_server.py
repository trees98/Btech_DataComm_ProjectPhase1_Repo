from socket import *

def start_server():
    #Create the server TCP socket
    server_port = 15000
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('192.168.71.104', server_port))
    server_socket.listen(1)
    print("The server is ready to receive...")
    return server_socket

def handle_client(connection_socket, addr):
    #Execute the input from the client to determine if a number is even or odd
    print("Connection established with:", addr)

    try:
        while True:
            message = connection_socket.recv(2048)
            if not message:
                break  
            #Client is disconnected

            modified_message = message.decode()

            if modified_message.lower() == 'exit':
                print("Exit command recieved from client.")
                connection_socket.send("Server shutting down".encode())
                connection_socket.close()
                return 'exit'
            try:
                number = int(modified_message)
                if number % 2 == 0:
                    response = f"{number} is even."
                else:
                    response = f"{number} is odd."
            except ValueError:
                response = "Please enter a valid number"

            connection_socket.send(response.encode())

#Save resources by closing the connection
    finally:
        connection_socket.close()
        print("Connection closed with:", addr)

def main():
    #Start the server and call functions
    server_socket = start_server()

    while True:
        connection_socket, addr = server_socket.accept()
        result = handle_client(connection_socket, addr)

        if result == 'exit':
            print("Server shutting down")
            server_socket.close()
            break

main()

