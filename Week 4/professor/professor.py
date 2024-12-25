
import random


def main():
    score = 0
    lvl = get_level()
    for i in range(10):
        x = generate_integer(lvl)
        y = generate_integer(lvl)
        correct = x+y

        for j in range(3):
            answer = input(f"{x} + {y} = ").strip()
            if answer.isnumeric() and int(answer) == correct:
                score += 1
                break
            else:
                print("EEE")
        else:
            print(f"{x} + {y} = {correct}")
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            assert 1 <= level <= 3
            return level
        except (ValueError, AssertionError):
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, int(10**level)-1)
    else:
        return random.randint(int(10**(level-1)), int(10**level)-1)


if __name__ == "__main__":
    main()
