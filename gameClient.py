import socket

print(f"Hello! This is to show the microservice is working and will send data back over to the client.  For this"
      f"microservice, it reaches out to the Board Game Geek API and receives the hottest board games and returns"
      f"them here, in a ranked list.")

user_input = input("If you would like to see the microservice in action, type in 'see games: ")

if user_input.lower() == 'see games':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 32000))

    server_message = client_socket.recv(4096).decode()
    print(server_message)

    client_socket.close()
