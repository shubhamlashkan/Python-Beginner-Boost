import random

secret_number = random.randint(1,100)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 100"))
    attempts = attempts+1
    if guess<secret_number:
        print("Input a higher number")
    elif guess>secret_number:
        print("Input a lower number")
    else:
        print(f"Congratulations you have taken {attempts} attempts")
        break

print("Bye")