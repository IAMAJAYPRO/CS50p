
def main():
    while True:
        try:
            frac = input("Fraction: ")
            percent = convert(frac)
            break
        except (ValueError, AssertionError, ZeroDivisionError):
            pass
    print(gauge(percent))


def convert(fraction):
    x, y = [int(x) for x in fraction.split("/")]
    assert 0 <= x/y <= 1
    return round(x*100 / y)


def gauge(percentage):
    if percentage <= 1:
        return ("E")
    elif percentage >= 99:
        return ("F")
    else:
        return (f"{percentage}%")


if __name__ == "__main__":
    main()
