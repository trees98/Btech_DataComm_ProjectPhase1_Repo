from socket import *

def connect_to_server(server_ip, server_port):
    #Create a TCP socket and establish a connection.
    try:
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        print("You have connected")
        return client_socket
    except:
        print("There was an issue establishing a connection:")
        return None

def send_and_receive(client_socket):
    #Handle sending messages and receiving responses.
    try:
        while True:
            message = input("Enter a number to check if it's even or odd (or 'exit' to quit): ")

            if message.lower() == "exit":
                client_socket.send(message.encode())
                print("Disconnecting... \nYou have disconnected")
                break

            client_socket.send(message.encode())
            response = client_socket.recv(2048).decode()
            print("From Server:", response)
    except:
        print("Please enter an int.")
#Specify the server IP and port number and call functions
def main():
    server_name = '127.0.0.1' #Change to server IP
    server_port = 15000

    client_socket = connect_to_server(server_name, server_port)
    if client_socket:
        try:
            send_and_receive(client_socket)
        finally:
            client_socket.close()

main()


