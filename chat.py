import socket
import threading

HOST = '127.0.0.1'  # Localhost
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server is waiting for connection...")
conn, addr = server.accept()
print(f"Connected by {addr}")

def receive_messages():
    while True:
        try:
            message = conn.recv(1024).decode()
            if message:
                print("\nClient:", message)
        except:
            print("Connection closed.")
            conn.close()
            break

def send_messages():
    while True:
        message = input("You: ")
        conn.send(message.encode())

# Run send and receive simultaneously
threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()
