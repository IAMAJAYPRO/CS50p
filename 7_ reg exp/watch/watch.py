import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern_link = r"https?://(?:www\.)?youtube\.com/embed/([\w-]+)"
    pattern = r"< *iframe.*"+pattern_link+r".*>"
    link = re.search(pattern, s)
    if link:
        id = link.group(1)
        return r"https://youtu.be/"+id
    else:
        return


...


if __name__ == "__main__":
    main()
