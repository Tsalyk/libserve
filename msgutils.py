from socket import socket

default_header_size = 10
default_size_pack = 5


def sendMsg(message: bytes,
            conn: object,
            header_size: int = default_header_size) -> bool:
    size_message = f"{len(message):{(header_size)}}"

    if conn.send(size_message.encode('866')) != header_size:
        print("ERROR: can't send size message")
        return False

    if conn.send(message) != len(message):
        print("ERROR: can't send message")
        return False

    return True

def readMsg(conn: object,
            header_size: int = default_header_size,
            size_pack: int = default_size_pack):
    data = conn.recv(header_size)

    if not data or len(data) != header_size:
        print("ERROR: can't read size message")
        return False

    size_msg = int(data.decode('866'))
    msg = b""

    while True:
        if size_msg <= size_pack:
            pack = conn.recv(size_msg)
            if not pack:
                return False

            msg += pack
            break

        pack = conn.recv(size_pack)
        if not pack:
            return False

        size_msg -= size_pack
        msg += pack

    return msg.decode('866')