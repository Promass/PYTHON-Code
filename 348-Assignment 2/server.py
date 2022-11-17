import socket
import serverfunctions
import pickle

dataset = serverfunctions.loadData("data.txt")
print(serverfunctions.printReport(dataset))

'''server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 9999))
server.listen(1)

while True:
    clientsocket, address = server.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))

    while True:
        request = clientsocket.recv(4096)
        request = request.decode("utf-8")

        match request:
            case "1":
                clientsocket.send(bytes("Received 1", "utf-8"))
            case "2":
                clientsocket.send(bytes("Received 2", "utf-8"))
            case "7":
                msg = pickle.dumps(dataset)
                clientsocket.send(bytes(msg, "utf-8"))
'''