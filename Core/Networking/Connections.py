import socket

from Networking.Connection import Connection
class Connections:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_accept(self):
        self.server.bind(('0.0.0.0', 9339))
        print("Server launched.")
        while True:
            self.server.listen()
            socket, address = self.server.accept()
            print(f'New connection!')
            Connection(socket, address).start()