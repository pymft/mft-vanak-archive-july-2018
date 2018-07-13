import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
proxy.db.write('hello\n')
proxy.db.write('hello\n')
proxy.db.disconnect()