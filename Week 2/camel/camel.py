sent = input("camelCase")
ne = ""
for i in sent:
    if i.islower():
        ne += i
    else:
        ne += "_"
        ne += i.lower()
print(ne)
