import socket

ip = "127.0.0.1"
port = 12345
server_addr = (ip, port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(server_addr)
print(f"Server is listening on {ip}:{port}")

while True:
    data, client_addr = server_socket.recvfrom(1024)

    print(f"ได้รับข้อความจาก {client_addr}: {data.decode()}")

    response_message = f"Server: ได้รับข้อความของคุณเเล้ว"
    server_socket.sendto(response_message.encode(), client_addr)
    