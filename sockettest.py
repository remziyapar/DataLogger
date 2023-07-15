import socket
user={}



class SocketIslem(object):
    hostname, sld, tld, port = 'www', 'integralist', 'co.uk', 80
    target = '{}.{}.{}'.format(hostname, sld, tld)
    def __init__(self, host):
        self.host = host
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, 502))
        client.settimeout(0)
        self.client = client
        user[host] =self.client


    def send(self, data):
        self.data = data
        self.client.send(data)

    def recv2(self):
        response = self.client.recv(512)
        return response

    def close(self):
        self.client.close()
