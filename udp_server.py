from socket import * #import everything from socket module

#function for UDP ECHO server, listens to incoming messages on specific port
#converts messages to upper case and sends back to client
#shuts down if Ctrl+C is pressed or when it recieves shutdown command from a client
def udp_server(port=12000):
    server_socket = socket(AF_INET, SOCK_DGRAM) #creates UDP socket using IPv4 and datagram socket
    
    #bind the socket to all available interfaces ("") on the given port
    server_socket.bind(("", port)) #listen for any incoming UDP messages 

    server_socket.settimeout(1.0)  #set timeout to block operations like recvfrom() allowing loop to check for keyboard interupt

    print(f"UDP Server is ready to receive on port {port}")

    #try block for error handling
    try:
        while True: #start loop to continuously recieve messages 
            try: #try to recieve data from any client
                message, client_address = server_socket.recvfrom(2048)
                decoded_msg = message.decode() #decode message recieved from bytes into string

                if decoded_msg.lower() == "shutdown": #if the decoded message is shutdown
                    print("Shutdown command received. Server shutting down.")
                    server_socket.sendto("Server shutting down.".encode(), client_address) #let client know server is shutting down
                    break #break out of main loop to shutdown server

                modified_message = decoded_msg.upper() #if its a normal message, decode and convert to upper case
                server_socket.sendto(modified_message.encode(), client_address) #send message back to client

            except timeout: #if no message recieved in 1 sec, continue loop, keeps server responsive to keyboardinterupt
                continue

    except KeyboardInterrupt: #catch manual interuption and exit
        print("\nServer shutting down via Ctrl+C")

    finally:
        server_socket.close() #close server socket
        print("Socket closed.")

udp_server() #call function to start udp server