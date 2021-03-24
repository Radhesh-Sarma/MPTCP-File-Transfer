
class Util:
    def recvall(self, length):
        data = b''
        rem = length
        while rem > 0:
            try:
                new_data = self.sock.recv(rem)
                if not new_data:
                    raise Exception('peer closed')
                data += new_data
            except socket.timeout as e:
                # TODO: handle several timeouts (probably lost connection)
                pass
            rem = length - len(data)
        return data