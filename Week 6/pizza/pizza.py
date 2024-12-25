import sys
from tabulate import tabulate
import csv
if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].lower().endswith(".csv"):
    sys.exit("Not a CSV file")
file = sys.argv[1]
data = []
try:
    with open(file) as f:
        reader = csv.reader(f)
        data = [x for x in reader]
except FileNotFoundError:
    sys.exit("File does not exist")

art = tabulate(data[1:], data[0], tablefmt="grid")
print(art)
