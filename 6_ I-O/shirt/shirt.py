import sys
from PIL import Image, ImageOps


if len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")


def matchExt(f1: str, f2: str):
    return f1.split(".")[-1].lower() == f2.split(".")[-1].lower()


file, to = sys.argv[1:3]
if not matchExt(file, to):
    sys.exit("Input and output have different extensions")

shirt = Image.open(
    "shirt.png")
try:
    with Image.open(file) as im:
        im = ImageOps.fit(im, size=[600, 600])
        im.paste(shirt, mask=shirt)
        im.save(to)
        shirt.close()
except FileNotFoundError:
    sys.exit("Input does not exist")
