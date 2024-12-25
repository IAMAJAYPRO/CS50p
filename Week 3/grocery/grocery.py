di = {}
while True:
    try:
        item = input().strip().upper()
        di[item] = di.get(item, 0)+1
    except EOFError:
        break
for item_, ct in sorted(di.items()):
    print(ct, item_)
