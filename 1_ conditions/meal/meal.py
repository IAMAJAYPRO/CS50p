def main():
    timeStr = input("What time is it? ")
    time = convert(timeStr)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time: str):
    hr, min = [int(x) for x in time.split(":")]
    return hr + min/60


if __name__ == "__main__":
    main()
