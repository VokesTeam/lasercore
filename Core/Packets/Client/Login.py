from ..PiranhaMessage import PiranhaMessage


class Login(PiranhaMessage):
    def __init__(self, client, player, initial_bytes):
        self.client = client
        self.player = player
        super().__init__(initial_bytes)
        

    def decode(self):
        self.ID = self.r.readLong()

    def process(self):
        print(self.ID)