import socket
def server_program():
    port = 9000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    server_socket.bind(("", port))  # bind host address and port together

    server_socket.listen(5)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection
server_program()
