def is_vowel(ch:str):
    return ch.lower() in "aeiou"


def main():
    st = input("Input: ")
    print("Output:", shorten(st))


def shorten(word):
    ne = ""
    for i in word:
        if not is_vowel(i):
            ne += i
    return ne


if __name__ == "__main__":
    main()
