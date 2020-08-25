import socket
import pickle
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(), 8900))
    s.settimeout(10)
    try:
        s.listen(5)
        print("Server is up and listening for connections..")
        a = {'a':1, 'b':2}
        pickled_dict = pickle.dumps(a)
        client, address = s.accept()
        print("Connection Established", address, 'Successfull')
        print("Client details, ", client)
        #client.send(bytes("Hello Welcome to socket programming.", "utf-8"))
        client.send(pickled_dict)
    except socket.timeout:
        print("Socket connection closed due to timeOut, GoodBye")
