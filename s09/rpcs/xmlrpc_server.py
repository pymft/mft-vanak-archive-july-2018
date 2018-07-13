from xmlrpc.server import SimpleXMLRPCServer

class ConnectToFile:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.f = open('my_data.txt', 'at')

    def write(self, val):
        self.f.write(val)

    def closefile(self):
        self.f.close()


inst = ConnectToFile()

server = SimpleXMLRPCServer(("localhost", 8000))

server.allow_none = True
server.allow_dotted_names = True
print("Listening on port 8000...")
server.register_function(inst.write, "db.write")
server.register_function(inst.closefile, "db.disconnect")
server.serve_forever()
