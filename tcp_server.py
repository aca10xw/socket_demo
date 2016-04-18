import socket
import threading
import time

thread_lock = threading.Lock()

def tcp_link(sock, addr):
    channel_closed = False

    while True:

        data = sock.recv(1024)  # nothing below this line will be executed until server receive a patch of new data
        if data == 'exit' or not data:
            channel_closed = True
            break
        else:
            sock.send(data.upper())

    if channel_closed:
        print 'Shutting down connection from {}'.format(addr)
        sock.send('shutdown')
        sock.shutdown(socket.SHUT_RDWR)
        print 'Service to {} has been completed shut down'.format(addr)


class TcpLink(threading.Thread):
    def __init__(self, sock, addr):
        threading.Thread.__init__(self)
        self.sock = sock
        self.addr = addr

    def run(self):
        # thread_lock.acquire()
        tcp_link(self.sock, self.addr)
        # thread_lock.release()


def main():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('127.0.0.1', 9999))
        s.listen(5)
        sock, addr = s.accept()  # nothing below this line will be executed until server receive a new connection
        t = TcpLink(sock, addr)
        t.start()

if __name__ == '__main__':
    main()
