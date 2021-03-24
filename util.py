
class Util:
    '''
    Helper functions
    '''
    def recvall_file(filename, sock, delimiter):
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

    def recvall(sock, delimiter):
        data = b''
        while True:
            more = sock.recv(1)
            if more == delimiter:
                break
            data += more
        return data