months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
]
while True:
    try:
        # month date year
        date = input("Date: ").strip().lower()
        if "/" in date:
            date_arr = [int(x) for x in date.split("/")]

        else:
            rst, year = date.split(",")
            year = year.strip()
            month, date = rst.split()
            month = months.index(month)+1
            date_arr = [int(x) for x in [month, date, year]]
        month, date, year = date_arr
        assert len(date_arr) == 3
        assert 1 <= date_arr[0] <= 12  # month
        assert 1 <= date_arr[1] <= 31  # date

        break

    except (AssertionError, ValueError, EOFError):
        pass


print(f"{year:04}-{month:02}-{date:02}")

