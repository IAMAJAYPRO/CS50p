import inflect
names = []
while True:
    try:
        name = input("Name: ").strip()
    except EOFError:
        break
    if name == "":
        break
    else:
        names.append(name)

p=inflect.engine()

str_to_print = "Adieu, adieu, to " + p.join(names)
print(str_to_print)

# original
"""
def make_adew(names_):
    if len(names_) > 1:
        return names_[0]+", " + make_adew(names_[1:])  # reduce 1
    else:
        return "and " + names_[0]


if len(names) == 1:
    str_to_print = "Adieu, adieu, to " + names[0]
else:
    str_to_print = "Adieu, adieu, to " + make_adew(names)
"""
