import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^" + r"(\d+)\."*3 + r"(\d+)$"
    nums = re.search(pattern, ip)

    if nums:
        for i in nums.groups():
            if not 0 <= int(i) <= 255:
                return False
        else:
            return True
    else:
        return False


...


if __name__ == "__main__":
    main()
