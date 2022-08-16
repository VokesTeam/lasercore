from threading import Thread
import time
import traceback

from Logic.Player import Player
from Packets.Factory import packets


class Connection(Thread):
    def __init__(self, client, address):
        super().__init__()
        self.address = address
        self.client = client
        self.player = Player()
        self.timeout = time.time()

    def recvall(self, zhezhka):
            data = bytearray()
            while len(data) < zhezhka:
                packet = self.client.recv(zhezhka - len(data))
                if not packet:
                    return None
                data.extend(packet)
            return data

    def run(self):
        try:
            while True:
                data = self.client.recv(7)
                if len(data):
                    id = int.from_bytes(data[:2], 'big')
                    length = int.from_bytes(data[2:5], 'big')
                    version = int.from_bytes(data[5:7], 'big')
                    data = self.recvall(length)
                    print(f'Received new packet: ID: {id}, Length: {length}, Version: {version}')
                    if id in packets:
                        message = packets[id](self.client, self.player, data)
                        message.decode()
                        message.process()
                    
                

                if time.time() - self.timeout > 7:
                    print(f"Client disconnected!")
                    self.client.close()
                    return

        except ConnectionError:
            print(f"Client disconnected!")
            self.client.close()
            print(traceback.format_exc())
            return

        except OSError:
            print(f"Client disconnected!")
            self.client.close()
            print(traceback.format_exc())
            return

        except:
            print(traceback.format_exc())
            return