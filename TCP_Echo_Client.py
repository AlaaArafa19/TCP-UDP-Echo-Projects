import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's port
server_address = ('localhost', 10000)
print('Connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    # Send data
    message = 'Hello, this is a test message!'
    print('Sending: "%s"' % message)
    sock.sendall(message.encode('UTF-8'))

    # Look for the response
    amount_received = 0
    amount_expected = len(message.encode('UTF-8'))
    
    while amount_received < amount_expected:
        # Receive in 16-byte chunks to match the server buffer size
        data = sock.recv(16)
        amount_received += len(data)
        print('Received back: "%s"' % data.decode('UTF-8'))

finally:
    # Clean up the socket connection
    print('Closing socket')
    sock.close()