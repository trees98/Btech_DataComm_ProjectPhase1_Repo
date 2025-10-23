from socket import * #import everything from socket module
    
    #his funcion creates a UDP client that sends messages to a UDP server and recieves responses
    #server IP and port passed as perameters with defaults
def udp_client(server_ip="10.10.10.1", server_port=12000):
 
    #creates UDP socket using IPv4 addressing and datagram socket type
    client_socket = socket(AF_INET, SOCK_DGRAM)

    try: #try block for error handling
        while True: #main loop to get user input and talk with server
            message = input("Enter message (or type 'quit' to exit): ") #user prompt

            if message.lower() == "quit": #if user enters quit
                
                client_socket.sendto("shutdown".encode(), (server_ip, server_port)) #send shutdown to the server
                modified_message, server_address = client_socket.recvfrom(2048) #wait to recieve servers shutdown confirmation
                print("From server:", modified_message.decode()) #decode the confirmation from server and print to screen
                print("Closing socket.") #let user know socket closing
                break #break from loop and end program

            client_socket.sendto(message.encode(), (server_ip, server_port)) #if input is not quit, encode and send normal message to server

            modified_message, server_address = client_socket.recvfrom(2048) #wait to recieve servers response message
            print("From server:", modified_message.decode()) #decode and print servers response 

    except Exception as e: #catch any exceptions or errors 
        print("Error:", e) #print the error

    finally: #runs at end, ensurees socket closes 
        client_socket.close()

udp_client() #call the function to start UDP client (no perameteres passed so default values used)