import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_ip = "127.0.0.1"
server_port = 12345
server_address = (server_ip, server_port)

while True:
    message = input("พิมพ์ข้อความที่ต้องการส่ง : ")
    if(message.lower() == "exit"):
        print("ปิดการเชื่อมต่อ")
        break

    client_socket.sendto(message.encode(), server_address)

    data, _ = client_socket.recvfrom(1024)
    print(data.decode())

client_socket.close()