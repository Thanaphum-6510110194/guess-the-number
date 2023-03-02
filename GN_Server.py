import random
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


def handle_client(conn, addr):
    print('Connected by', addr)
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    num_guesses = 1

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            guess = int(data.decode())
            
            if num_guesses > 9:
                message = "You lose!"
                conn.sendall(message.encode())
                break

            num_guesses += 1
            if guess < secret_number:
                message = f"Your guess of {guess} is too low"
            elif guess > secret_number:
                message = f"Your guess of {guess} is too high"
            else:
                message = "You win!"
                conn.sendall(message.encode())
                break

            conn.sendall(message.encode())

        except ValueError:
            conn.sendall("Invalid input, please enter a number between 1 and 100".encode())

    # Close the client connection
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        handle_client(conn, addr)
