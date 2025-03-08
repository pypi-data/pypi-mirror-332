import socket

class Client:
    def __init__(self, host="127.0.0.1", port=65432):
        self.host = host
        self.port = port

    def send_message(self, message):
        """Send a message to the server."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.host, self.port))
            sock.sendall(message.encode())
            response = sock.recv(1024).decode()
            return response
