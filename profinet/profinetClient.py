import socket
import struct

def profinet_client(server_ip, server_port, send_integer):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    server_address = (server_ip, server_port)
    client_socket.connect(server_address)
    
    try:
        # Send an integer to the server
        data = struct.pack('!i', send_integer)
        client_socket.sendall(data)
        print(f"Sent integer: {send_integer}")
        
        # Receive an integer from the server
        data = client_socket.recv(4)  # Expecting 4 bytes for an integer
        if data:
            received_integer = struct.unpack('!i', data)[0]
            print(f"Received integer: {received_integer}")
    
    finally:
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    send_integer = 42  # Example integer to send
    profinet_client('192.168.1.201', 102, send_integer)
