import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('', 4443))

sock.listen(10)

print "watiing for client "

(client, (ip, port)) = sock.accept()

print 'Received connaction from:', ip
data = client.recv(1024)

while True:

    print data

    cmd = raw_input()
    client.send(cmd)
    print data
client.close()
