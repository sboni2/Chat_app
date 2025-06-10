import socket
import threading

clients = []
usernames = []

def broadcast(message, _client_socket):
    for client in clients:
        if client != _client_socket:
            client.send(message)

def handle_client(client_socket):
    try:
        # First message is the username
        username = client_socket.recv(1024).decode('utf-8')
        usernames.append(username)
        clients.append(client_socket)
        broadcast(f"[{username} joined the chat]".encode('utf-8'), client_socket)
        print(f"{username} connected.")
        
        while True:
            msg = client_socket.recv(1024)
            if not msg: break
            broadcast(f"{username}: {msg.decode('utf-8')}".encode('utf-8'), client_socket)
    finally:
        idx = clients.index(client_socket)
        client_socket.close()
        clients.remove(client_socket)
        left_username = usernames.pop(idx)
        broadcast(f"[{left_username} left the chat]".encode('utf-8'), None)
        print(f"{left_username} disconnected.")

def main():
    host = "0.0.0.0"
    port = 12345
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"Server listening on {host}:{port}")
    
    while True:
        client_sock, addr = server.accept()
        threading.Thread(target=handle_client, args=(client_sock,)).start()

if __name__ == "__main__":
    main()
