## 💬 Python CLI Chat Application

A simple, pure‑Python client-server chat app using sockets and threads. It enables real-time messaging between multiple users on the same network (`127.0.0.1:5050`).

### 🔑 Core Features

* **Multi-threaded Server**
  Listens on `127.0.0.1:5050`, accepts new client connections, and starts a new thread for each client to handle messages and disconnections.

* **Client in Same Script**
  Connects to the server, starts a listener thread to display incoming messages, and allows sending chat messages until the user types `exit`.

* **Broadcast System**
  Messages are relayed to all connected clients—simple and effective for local chat.

### 📋 Sample Output

```
[LISTENING] Server is listening on 127.0.0.1:5050
[NEW CONNECTION] ('127.0.0.1', 12345) connected.
Hello from client!
Hello from server!
How are you?
I'm fine, thank you!
exit
[DISCONNECTED] ('127.0.0.1', 12345) disconnected.
```

This demonstrates a typical session:

1. Server starts and listens.
2. A client connects (`12345` is its port).
3. A conversation takes place.
4. The client exits, and the disconnection is logged.

### ⚙️ How to Run

1. **Launch the server‑client script**:

   ```bash
   python chat_app.py
   ```
2. Open another terminal and **run the script again** to start a new client.
3. **Exchange messages** interactively. Type `exit` to leave the chat.

### 🧠 Next Steps

* Split into `server.py` and `client.py` for modularity.
* Add usernames to clearly identify senders.
* Enhance error handling for more robust networking.
* Consider using `asyncio` or encryption for advanced use cases.



