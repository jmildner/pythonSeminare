import random

print("Übung 5.6 - guess a number between 1 and 100")

guess = 0
n = 100
to_be_guessed = int(n * random.random()) + 1

while guess != to_be_guessed:
    guess = int(input("guess a number > "))
    if guess > 0:
        if guess > to_be_guessed:
            print("number too big")
        elif guess < to_be_guessed:
            print("number too small")
    else:
        print("what a pity, you quit")
        break
else:
    print("Congratulation! You got it")
