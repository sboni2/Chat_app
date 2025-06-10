import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 5050

# List to store connected clients
clients = []

# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")

    # Add client to the list
    clients.append(client_socket)

    # Loop to receive and broadcast messages
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            # Broadcast message to all clients
            broadcast(message)
        except:
            break

    # Close client connection
    print(f"[DISCONNECTED] {client_address} disconnected.")
    clients.remove(client_socket)
    client_socket.close()

# Function to broadcast message to all clients
def broadcast(message):
    for client in clients:
        client.send(message.encode('utf-8'))

# Function to receive messages from server
def receive_messages(client_socket):
    while True:
        try:
            # Receive message from server
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            # Handle disconnection
            print("[ERROR] Connection to server lost.")
            break

# Main function to start the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

    while True:
        # Accept incoming connection
        client_socket, client_address = server.accept()
        
        # Handle client connection in a separate thread
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

# Main function to start the client
def start_client():
    # Connect to server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    # Start thread to receive messages
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    # Main loop to send messages
    while True:
        message = input()
        if message.lower() == 'exit':
            break
        client.send(message.encode('utf-8'))

    # Close connection
    client.close()

# Start the server and client
if __name__ == "__main__":
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    start_client()
