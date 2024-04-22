def main():
    sent = input("Greeting: ").lower().strip()
    print(f"${value(sent)}")


def value(greeting: str):
    greet = greeting.lower()
    if greet.startswith("hello"):
        return 0
    elif greet.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
