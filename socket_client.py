import socket
import time

sock1 = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

sock1.connect("/home/korisnik/sock1.socket")
poruka = str(time.time())
sock1.send(poruka.encode("UTF-8"))
