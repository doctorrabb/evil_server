import socket
import sys

class Listener (object):
    def __init__(self, addr, port, payload):
        self.addr = addr
        self.port = port
        self.payload = payload
        self.sock_init ()
        self.client_addrs_history = list ()

    def sock_init (self):
        self.sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt (socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind ((self.addr, self.port))
        self.sock.listen (3)

    def get_data (self):
        from core.const import RECV_BYTES
        from core.design.colors import INFO

        connection, addr = self.sock.accept ()
        data = connection.recv (RECV_BYTES)

        self.client_addrs_history.append (addr [0])

        print INFO + 'Client sent request. IP: {0}'.format(addr [0])

        connection.send ('')
        connection.close ()

        if data:
            return data

        return '\n'

    def send_data (self, text):

        from core.design.colors import INFO

        connection, addr = self.sock.accept()
        self.client_addrs_history.append(addr[0])

        print INFO + 'Client connected. IP: {0}'.format(addr[0])

        connection.send (text)
        connection.close ()

    def connection_execute(self, payload):
        from importlib import import_module
        from core.db.payloads_db import PayloadDB
        from core.const import PAYLOAD_DB_PATH

        db = PayloadDB (PAYLOAD_DB_PATH)
        FULL_NAME = str ()
        IS_OK = False

        for i in db.get_payloads ():
            if i ['short'] == payload:
                IS_OK = True
                FULL_NAME = i ['path']
                break

        if IS_OK:
            payload_exec = getattr (import_module ('payloads.{0}'.format (FULL_NAME)), 'Payload') (self)
            payload_exec.run ()
        else:
            from core.design.colors import ERR
            print ERR + 'No such payload: {0}'.format (payload)
            sys.exit (-1)

    def start_listen (self):

        while True:
            try:
                self.connection_execute (self.payload)
                self.sock_init ()

            except KeyboardInterrupt:

                from core.design.banners import show_date

                show_date ('Finish')
                sys.exit (0)


