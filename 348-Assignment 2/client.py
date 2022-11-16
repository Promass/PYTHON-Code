# cd 'PYTHON-Code/348-Assignment 2'

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((socket.gethostname(), 9999))

message = server.recv(4096)
print(message.decode("utf-8"))

while True:
    print("Python DB Menu\n")
    print("1. Find customer")
    print("2. Add customer")
    print("3. Delete customer")
    print("4. Update customer age")
    print("5. Update customer address")
    print("6. Update customer phone")
    print("7. Print report")
    print("8. Exit\n")

    user_input = input("Select: ")

    match user_input:
        case "1":
            server.send(bytes("1", "utf-8"))
        case "2":
            server.send(bytes("1", "utf-8"))
        case "7":
            server.send(bytes("7", "utf-8"))
        case "8":
            break

    server_output = server.recv(4096)
    print("\n")
    print(server_output)
    print("\n")
