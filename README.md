## 💬 Python CLI Chat Application

A simple client-server chat application built entirely in Python, enabling real-time message exchange over TCP sockets.

### 🔑 Core Features

* **Multi-threaded Server:** Handles multiple clients concurrently via separate Client threads—each user connects to `127.0.0.1:5050` and is served in isolation. When a client sends a message, it’s **broadcast to all connected users** ([github.com][1], [github.com][2]).

* **Client Module:** Upon launching, the client connects to the server, starts a receive loop in a background thread to display incoming messages, and allows users to send messages until typing `'exit'`.

* **Session Management:** Tracks connected clients in a `clients` list. Handles disconnections cleanly—when a client leaves, it's removed from the list, and the connection is closed.

---

### 🧠 Why It Works Well

* **Asynchronous Handling:** The server uses threading to ensure interactions are non-blocking and responsive ([linkedin.com][3]).
* **Scalable Design:** Supports multiple CLI clients running in separate terminals—perfect for local chat testing.
* **Pure Python:** Relies solely on built-in modules—`socket` for networking, `threading` for concurrency. No external dependencies required.

---

### 🚀 How to Run

1. **Start the server**:

   ```bash
   python your_script.py
   ```

   You’ll see output along the lines of:

   ```
   [LISTENING] Server is listening on 127.0.0.1:5050
   ```

2. **Connect the client** (in a separate terminal):

   ```bash
   python your_script.py
   ```

   Or run the script again—one process acts as the server, another as the client. Type messages to chat; type `exit` to disconnect.
   
3. **Output**
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
   
 

4. **Chat Between Multiple Clients:** Open more terminals and run the client code to simulate a group chat.

---

### ⚙️ Potential Enhancements

* Split into **dedicated `server.py` and `client.py`** for better separation.
* Add **usernames** for message attribution.
* Improve error resilience with exception handling for network failures.
* Explore **asynchronous approaches** via `asyncio` or `selectors` for more scalable concurrency .

