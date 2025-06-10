import socket
import threading

def receive(sock):
    while True:
        try:
            msg = sock.recv(1024).decode('utf-8')
            if msg:
                print(msg)
            else:
                break
        except:
            break

def main():
    host = input("Enter server IP (e.g. 127.0.0.1): ")
    port = int(input("Enter port: "))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    username = input("Choose a username: ")
    client.send(username.encode('utf-8'))

    threading.Thread(target=receive, args=(client,), daemon=True).start()

    print("Type 'exit' to quit.")
    while True:
        msg = input()
        if msg.lower() == "exit":
            break
        client.send(msg.encode('utf-8'))

    client.close()

if __name__ == "__main__":
    main()
