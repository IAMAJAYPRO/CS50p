def solve(string: str):
    match string:
        case _ if "+" in string:
            expr = "+"
        case _ if "-" in string:
            expr = "-"
        case _ if "*" in string:
            expr = "*"
        case _ if "/" in string:
            expr = "/"
        case _:
            return

    x, y = [int(x) for x in string.split(expr)]
    return eval(f"{float(x)}{expr}{y}")


inp = input("Expression: ")
print(solve(inp))
