import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432    # The port used by the server


def get_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 100:
                raise ValueError("Guess must be between 1 and 100")
            return guess
        
        except ValueError as E:
            print(str(E))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Guess the number between 1 and 100!")
    while True:
        guess = get_guess()
        s.sendall(str(guess).encode())
        data = s.recv(1024)
        print(data.decode())
        if "You win!" in data.decode():
            print("Congratulations, you won!")
            break
        elif "You lose!" in data.decode():
            print("Sorry, you lost. Too many guesses.")
            break
        
print("Thanks for playing!")
