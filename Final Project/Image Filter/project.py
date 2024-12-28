import argparse
from filters import available_filters, np, Image, ImageFilter


def main():
    args = command_prompt()
    input_img = Image.open(args.input).convert("RGB")
    output = args.output
    filter = args.filter
    img = available_filters[filter](input_img)
    if not output:
        img.show()
        return
    img.save(output)


def command_prompt():
    parser = argparse.ArgumentParser(description="Image Filters")
    parser.add_argument("input", help="Input image file to apply filter on.")
    parser.add_argument(
        "filter", help="Filter to apply on the image.", choices=available_filters.keys())
    parser.add_argument("output", default="", nargs="?",
                        help="Output file name to store the image. Dont use this for not saving.")

    parser.epilog = """Final Project by @IAMAJAYPRO. for CS50P"""
    return parser.parse_args()


if __name__ == "__main__":
    main()
