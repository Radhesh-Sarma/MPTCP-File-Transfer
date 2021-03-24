import socket,argparse

class FileClient:
    def __init__(self,client_address,server_address,filename):
        self.client_address = client_address
        self.server_address = server_address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(self.client_address)
        self.name = self.sock.getsockname()
        print('Client has been assigned socket name', self.name)
        self.sock.connect(self.server_address)
        input_file = open(filename, 'rb')
        block_size = 32
        snd_bytes = 0
        while True:
            piece = input_file.read(block_size)
            snd_bytes += block_size
            print('\r  %d bytes send' % (snd_bytes,), )
            if piece == "":
                piece = b'bye$'
                sock.sendall(piece)
                break # end of file

            self.sock.sendall(piece)
        input_file.close()
        message = Util.recvall(sock, b'$')
        print (message)
        self.sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser('File Transfer Client')
    parser.add_argument('--filename', type=str, default='file_sample1.mp4', help='video filename to stream')
    parser.add_argument('--server_ip', type=str, default='127.0.0.1', help='IP address of server')
    parser.add_argument('--server_port', type=int, default=5000, help='port number of server')
    parser.add_argument('--client_ip', type=str, default='127.0.0.1', help='IP address of client')
    parser.add_argument('--client_port', type=int, default=8000, help='port number of client')
    args = parser.parse_args()
    file_client = FileClient(client_address=(args.client_ip,args.client_port),server_address=(args.server_ip,args.server_port),filename=f'{args.filename}')