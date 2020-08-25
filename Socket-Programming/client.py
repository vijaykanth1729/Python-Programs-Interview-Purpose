import socket
import pickle
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((socket.gethostname(), 8900))

        while True:
            msg = s.recv(1024)
            if not msg:
                print("No more data from server..")
                break
            else:
                print("Message from server: ", pickle.loads(msg))
                # s.close()  -> we used context manager which auto closes connection.
    except ConnectionRefusedError:
        print("Connection Refused As Server Is Down.")
