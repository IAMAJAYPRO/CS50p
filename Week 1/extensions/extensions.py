


def print_file_type(file: str):
    file=file.lower().strip()
    if "." not in file:
        print("application/octet-stream")
        return

    file_extension: str = file.split(".")[-1]
    match file_extension:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")


# Example usage:

file = input("File name: ")
print_file_type(file)
