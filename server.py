import socket
from library import Book, People, Library
from msgutils import sendMsg, readMsg

readers_id = 0


def launch():
    """
    Launches server
    """
    global readers_id

    sock = socket.socket()
    sock.bind(('', 12345))
    sock.listen(1)

    conn, addr = sock.accept()

    name = readMsg(conn)
    surname = readMsg(conn)
    age = int(readMsg(conn))

    print(name)
    print(surname)
    print(age)

    sendMsg((name + '\n').upper().encode('utf-8'), sock)
    sendMsg((str(age) + '\n').upper().encode('utf-8'), sock)
    sendMsg((surname + '\n').upper().encode('utf-8'), sock)

    conn.close()

launch()