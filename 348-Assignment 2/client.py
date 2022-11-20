# cd 'PYTHON-Code/348-Assignment 2'
# comment all code to clarify
# other quality checks
# test all posibilites, make sure no crashes

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

    if (user_input == ""):
        print("\nPlease enter a number from 1 to 8\n")
        continue
    else:
        match user_input:
            case "1":
                customer_name = input("Customer Name: ")
                server.send(bytes("1", "utf-8"))
                server.send(bytes(customer_name, "utf-8"))
            case "2":
                customer_name = input("Customer Name: ")
                customer_age = input("Customer Age: ")
                customer_address = input("Customer Address: ")
                customer_phone = input("Customer Phone Number: ")
                server.send(bytes("2", "utf-8"))
                server.send(bytes(customer_name, "utf-8"))
                server.send(bytes(customer_age, "utf-8"))
                server.send(bytes(customer_address, "utf-8"))
                server.send(bytes(customer_phone, "utf-8"))
            case "3":
                customer_name = input("Customer Name: ")
                server.send(bytes("3", "utf-8"))
                server.send(bytes(customer_name, "utf-8"))
            case "4":
                customer_name = input("Customer Name: ")
                customer_age = input("Customer Age: ")
                server.send(bytes("4", "utf-8"))
                server.send(bytes(customer_name, "utf-8"))
                server.send(bytes(customer_age, "utf-8"))
            case "5":
                customer_name = input("Customer Name: ")
                customer_address = input("Customer Address: ")
                server.send(bytes("5", "utf-8"))
                server.send(bytes(customer_name, "utf-8"))
                server.send(bytes(customer_address, "utf-8"))
            case "6":
                customer_name = input("Customer Name: ")
                customer_phone = input("Customer Phone Number: ")
                server.send(bytes("6", "utf-8"))
                server.send(bytes(customer_name, "utf-8"))
                server.send(bytes(customer_phone, "utf-8"))
            case "7":
                server.send(bytes("7", "utf-8"))
            case "8":
                server.send(bytes("8", "utf-8"))
                break
            case _:
                print("\nInvalid command\n")
                continue

        server_response = server.recv(4096)
        server_response = server_response.decode("utf-8")

        print(server_response)