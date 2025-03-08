import socket

class Server:
    def __init__(self, host="127.0.0.1", port=65432):
        self.host = host
        self.port = port

    def start(self):
        """Start the server and listen for incoming messages."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((self.host, self.port))
            sock.listen()
            print(f"Server listening on {self.host}:{self.port}")
            conn, addr = sock.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Received: {data.decode()}")
                    conn.sendall(data)  # Echo the received message back to the client
