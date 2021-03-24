import socket,argparse
from util import Util
class FileServer:
    def __init__(self,address,filename):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(address)
        self.name = self.sock.getsockname()
        self.sock.listen(5)
        print('Listening at', self.name)
        while True:
            sc, sockname = self.sock.accept()
            print('We have accepted a connection from', sockname)
            print('  Socket name:', sc.getsockname())
            print('  Socket peer:', sc.getpeername())
            Util.recvall(filename, sc, b'bye$')
            sc.sendall(b'Thank you$')
            sc.close()
            print('  Reply sent, socket closed')

if __name__ == "__main__":
    parser = argparse.ArgumentParser('File Transfer Client')
    parser.add_argument('--filename', type=str, default='server_recd.mp4', help='Video filename to stream')
    parser.add_argument('--server_ip', type=str, default='127.0.0.1', help='IP address of server')
    parser.add_argument('--server_port', type=int, default=5000, help='port number of server')
    args = parser.parse_args()
    file_server = FileServer(address=(args.server_ip,args.server_port),filename=f'{args.filename}')