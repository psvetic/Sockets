import socket
import time
import select

sock1 = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

sock1.bind("/home/korisnik/sock1.socket")
podaci = sock1.recv(4096)
primljeno = podaci.decode("UTF-8")
primljeno = float(primljeno)
vrijeme = time.time()
print(vrijeme, primljeno)
print(vrijeme - primljeno)
