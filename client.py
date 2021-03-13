import socket, time
from msgutils import sendMsg, readMsg

def launch():
    """
    Launches client's side
    """
    sock = socket.socket()
    sock.connect(('localhost', 12345))

    name = input("Enter your name: ")
    sendMsg(name.encode('866'), sock)

    surname = input("Enter your surname: ")
    time.sleep(0.1)
    sendMsg(surname.encode('866'), sock)

    age = input("Enter your age: ")
    time.sleep(0.1)
    sendMsg(age.encode('866'), sock)


    sock.close()

launch()