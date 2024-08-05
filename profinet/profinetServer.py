import socket
import struct

def start_profinet_server(host='0.0.0.0', port=102):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the address and port
    server_address = (host, port)
    server_socket.bind(server_address)
    
    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Profinet server listening on {host}:{port}")
    
    while True:
        # Wait for a connection
        connection, client_address = server_socket.accept()
        try:
            print(f"Connection from {client_address}")
            
            # Receive an integer from the client
            data = connection.recv(4)  # Expecting 4 bytes for an integer
            if data:
                received_integer = struct.unpack('!i', data)[0]
                print(f"Received integer: {received_integer}")

                # Process the received integer (for example, increment by 1)
                response_integer = received_integer + 1

                # Send the processed integer back to the client
                data = struct.pack('!i', response_integer)
                connection.sendall(data)
                print(f"Sent integer: {response_integer}")
        finally:
            # Clean up the connection
            connection.close()

if __name__ == "__main__":
    start_profinet_server()
