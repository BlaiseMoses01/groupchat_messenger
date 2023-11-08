# Implementation of a groupchat messenger server in python

# Import socket related methods
from socket import *

# Import argv related methods
from sys import *

# Import select method
from select import *


# Server needs the port number to listen on
if len(argv) != 2:
    print('usage:', argv[0], '<port>')
    exit()

# Get the port on which server should listen */
serverPort = int(argv[1])

# Create the server socket
serverSock = socket(AF_INET, SOCK_STREAM)

# Bind the socket to the given port
serverSock.bind(('', serverPort))

# Set the server for listening */
serverSock.listen()

# Make a list of inputs to watch for
inputSet = [serverSock]
client_reads = {}
client_names = {}

# Keep sending and receiving messages from the client
print('Waiting for clients...')
while True:

    # Wait for a message from client or server socket
    readableSet, x, x = select(inputSet,[],[])


    for item in readableSet:
        #establish new connections
        if item is serverSock:
            clientSock, clientAddr = serverSock.accept()
            clientSockFile = clientSock.makefile()
            name = clientSockFile.readline()
            inputSet.append(clientSock)
            client_reads[clientSock] = clientSockFile
            client_names[clientSock] = name
            print('Connected to ', name, ' at ', clientAddr)


        # Check if there is a message from the client
        else:

            # Read a message from the client
            line = client_reads[item].readline()

            # If EOF ==> client closed the connection
            if not line:
                print(client_names[item], ' closed connection')
                inputSet.remove(item)
                break

            # Send line to other clients,  but not the sender
            for sock in inputSet:
                if sock is not item:
                        if sock is not serverSock:
                            sock.send(client_names[item].encode())
                            sock.send(line.encode())



# close the connection
clientSockFile.close()
clientSock.close()



