import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_adress = ("localhost", 12345)
client_socket.connect(server_adress)

massage = "Привет, сервер!"
client_socket.send(massage.encode())

response = client_socket.recv(1024).decode()
print(f"Ответ от сервера: {response}")

client_socket.close()