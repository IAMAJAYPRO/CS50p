import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    words = re.split(r",", s)
    pattern = r"^um[.?]*($| )"
    ct = 0
    for word in words:
        word = word.strip().lower()
        if found := re.search(pattern, word, flags=re.IGNORECASE):
            ct += 1
            print(found)
    return ct


...


if __name__ == "__main__":
    main()
