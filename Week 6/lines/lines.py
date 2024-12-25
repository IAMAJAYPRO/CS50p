import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].lower().endswith(".py"):
    sys.exit("Not a Python file")
file = sys.argv[1]
ct = 0
try:
    with open(file) as f:
        for line in (line.strip() for line in f):
            if not (line.startswith("#") or line == ""):
                ct += 1
except FileNotFoundError:
    sys.exit("File does not exist")


print(ct)
