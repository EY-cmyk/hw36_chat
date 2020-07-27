import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect(('192.168.0.111', 5555))

config = {
    'name':'Dima'
}

connection_msg = '<' + config['name'] + ' connected>'
client_socket.sendall(str.encode(connection_msg))

while True:
    data = client_socket.recv(1024)

    #Обработка информации
    print(data.decode('utf-8'))

    if not data:
        break

client_socket.close()
