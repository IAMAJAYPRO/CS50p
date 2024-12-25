import random
import pyfiglet
import sys
args = sys.argv[1:]


fonts = pyfiglet.FigletFont.getFonts()
match len(args):
    case 0:
        font = random.choice(fonts)

    case 2 if args[0].strip() in ["-f", "--font"]:
        font = args[1]
        if font not in fonts:
            sys.exit("Invalid Font")

    case _:
        sys.exit("Invalid usage")

f = pyfiglet.Figlet(font=font)
print(f.renderText(input("Input: ")))
