from DataStream.ByteStream import Reader, Writer


class PiranhaMessage:
    def __init__(self, initial_bytes):
        self.r = Reader(initial_bytes)
        self.w = Writer(self.client)
    
    def encode(self): 
        pass

    def decode(self): 
        pass
    def process(self): 
        pass