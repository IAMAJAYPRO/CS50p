import random

while True:
    try:
        n = int(input("Level: "))
        assert n > 0
        break
    except (ValueError, AssertionError):
        pass

secret = random.randint(1, n)


while True:
    try:
        guess = int(input("Guess: "))
        assert guess > 0
    except (ValueError, AssertionError):
        pass
    else:
        if guess > secret:
            print("Too large!")
        elif guess < secret:
            print("Too small!")
        else:
            print("Just right!")
            break
