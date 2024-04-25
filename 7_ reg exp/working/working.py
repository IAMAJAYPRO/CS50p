import re
import sys


def main():
    print(convert(input("Hours: ")))


"""
9:00 AM to 5:00 PM
9 AM to 5 PM
12 AM to 12 PM
"""


def fix_hr(h, z):
    if h == 12:
        if z == "AM":
            return 0
        elif z == "PM":
            return 12
        else:
            raise ValueError
    else:
        h = (h + (12 if z == "PM" else 0)
             ) if z != "AM" or h != 12 else (0)
        return h


def validate(h1, m1, z1, h2, m2, z2):
    conditions = [
        0 <= int(h1) <= 12,
        0 <= int(h2) <= 12,
        z1 in ["AM", "PM"],
        z2 in ["AM", "PM"],

        0 <= int(m1) < 60 if m1 else True,
        0 <= int(m2) < 60 if m2 else True,
    ]

    if all(conditions):
        return True


def convert(s):
    t = r"(\d+)(?:\:(\d{2}))? (\w{2})"
    pattern = fr"{t} to {t}"

    time = re.search(pattern, s)
    if not time:
        raise ValueError("invalid format")
    # ('9', '00', 'AM', '5', '00', 'PM')
    h1, m1, z1, h2, m2, z2 = time.groups()

    if not validate(h1, m1, z1, h2, m2, z2):
        raise ValueError("Invalid input format")

    h1 = fix_hr(int(h1), z1)
    h2 = fix_hr(int(h2), z2)

    m1 = m1 if m1 else "00"
    m2 = m2 if m2 else "00"

    return f"{h1:02}:{m1} to {h2:02}:{m2}"


...


if __name__ == "__main__":
    main()
