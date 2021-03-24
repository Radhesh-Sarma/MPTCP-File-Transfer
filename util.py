
class Util:
    '''
    Helper functions
    '''
    def recvall(filename, sock, delimiter):
        file_ = open(filename, 'wb')
        recvd_bytes = 0
        data = b''
        while True:
            more = sock.recv(1024)
            data += more
            if data[-4:] == delimiter:
                break
            data = data[-10:]
            file_.write(more)
            file_.flush()
        file_.close()