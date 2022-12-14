import socket
import serverfunctions

#Insert data text file name here
DATA_FILE = "data.txt"

serverfunctions.loadData(DATA_FILE)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 9999))
server.listen(1)

while True:
    clientsocket, address = server.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("\nYou have successfully connected to the server!", "utf-8"))

    while True:
        client_request = clientsocket.recv(4096)
        client_request = client_request.decode("utf-8")

        match client_request:
            case "1":
                customer_name = clientsocket.recv(4096).decode("utf-8")
                if (customer_name != ""):
                    server_response = serverfunctions.findCustomer(customer_name)
                    clientsocket.send(bytes(server_response, "utf-8"))
                else:
                    clientsocket.send(bytes("Server received empty input", "utf-8"))
            case "2":
                customer_name = clientsocket.recv(4096).decode("utf-8")
                customer_age = clientsocket.recv(4096).decode("utf-8")
                customer_address = clientsocket.recv(4096).decode("utf-8")
                customer_phone = clientsocket.recv(4096).decode("utf-8")
                if (customer_name != "" and customer_age != "" and customer_address != "" and customer_phone != ""):
                    server_response = serverfunctions.addCustomer(customer_name, customer_age, customer_address, customer_phone)
                    clientsocket.send(bytes(server_response, "utf-8"))
                else:
                    clientsocket.send(bytes("Server received empty input", "utf-8"))
            case "3":
                customer_name = clientsocket.recv(4096).decode("utf-8")
                if (customer_name != ""):
                    server_response = serverfunctions.deleteCustomer(customer_name)
                    clientsocket.send(bytes(server_response, "utf-8"))
                else:
                    clientsocket.send(bytes("Server received empty input", "utf-8"))
            case "4":
                customer_name = clientsocket.recv(4096).decode("utf-8")
                customer_age = clientsocket.recv(4096).decode("utf-8")
                if (customer_name != "" and customer_age != ""):
                    server_response = serverfunctions.updateAge(customer_name, customer_age)
                    clientsocket.send(bytes(server_response, "utf-8"))
                else:
                    clientsocket.send(bytes("Server received empty input", "utf-8"))
            case "5":
                customer_name = clientsocket.recv(4096).decode("utf-8")
                customer_address = clientsocket.recv(4096).decode("utf-8")
                if (customer_name != "" and customer_address != ""):
                    server_response = serverfunctions.updateAddress(customer_name, customer_address)
                    clientsocket.send(bytes(server_response, "utf-8"))
                else:
                    clientsocket.send(bytes("Server received empty input", "utf-8"))
            case "6":
                customer_name = clientsocket.recv(4096).decode("utf-8")
                customer_phone = clientsocket.recv(4096).decode("utf-8")
                if (customer_name != "" and customer_phone != ""):
                    server_response = serverfunctions.updatePhone(customer_name, customer_phone)
                    clientsocket.send(bytes(server_response, "utf-8"))
                else:
                    clientsocket.send(bytes("Server received empty input", "utf-8"))
            case "7":
                server_response = serverfunctions.printReport()
                clientsocket.send(bytes(server_response, "utf-8"))
            case "8":
                break
            case _:
                clientsocket.send(bytes("Invalid user request", "utf-8"))