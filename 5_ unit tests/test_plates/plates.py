def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str):
    conditions = [
        s[:2].isalpha(),
        2 <= len(s) <= 6,
        not any([x in s for x in [". ,?"]])
    ]

    if not all(conditions):
        return False
    else:
        flag = False
        for i in range(len(s)):
            if s[i].isnumeric():
                flag = True
                init = i
                break
        if flag:
            return s[i:].isnumeric() and int(s[i]) != 0
        return True



"""
“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
"""

main()
