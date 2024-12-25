from datetime import date, timedelta
import inflect
import sys


def main():
    inp = input("Date of Birth: ").strip()
    dob = validate(inp)
    now = date.today()
    min_from: str = get_diff(dob, now)
    print(min_from, "minutes")


def validate(inp):
    try:
        dob = date.fromisoformat(inp)
    except ValueError:
        sys.exit("Invalid date")
    return dob


def get_diff(dob, now):
    p = inflect.engine()
    delta: timedelta = now-dob
    mins = round(delta.total_seconds()/60)
    num_word = p.number_to_words(mins, andword="")
    num_word = num_word[0].upper()+num_word[1:]
    return num_word


if __name__ == "__main__":
    main()
