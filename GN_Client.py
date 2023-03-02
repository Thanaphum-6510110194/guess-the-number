import socket

HOST = '127.0.0.1' # The server's hostname or IP address
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
           