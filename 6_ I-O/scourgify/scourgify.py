import sys
from tabulate import tabulate
import csv
if len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].lower().endswith(".csv"):
    sys.exit("Not a CSV file")
file = sys.argv[1]
to = sys.argv[2]
data = []
try:
    with open(file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            student = {}
            student["last"], student["first"] = [x.strip()
                                                 for x in row["name"].split(",")]
            student["house"] = row["house"]
            data.append(student)

except FileNotFoundError:
    sys.exit("File does not exist")
with open(to, "w") as f:
    writer = csv.DictWriter(f, fieldnames=["first", "last", "house"])
    writer.writeheader()
    writer.writerows(data)
