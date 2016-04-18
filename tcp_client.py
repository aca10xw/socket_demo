import socket

def talk_client(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = raw_input('->')

    while message != '!q':
        s.send(message)
        data = s.recv(1024)
        if data == 'shutdown':
            print 'This client is about to be shut down'
            break
        else:
            print 'Server: ' + data
            message = raw_input('->')
    s.close()
    print 'Ok, talk\'s over and connection closed'

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 9999

    try:
       talk_client(host, port)
    except socket.error:
       print 'Ok, talk\'s over - remote server error'
