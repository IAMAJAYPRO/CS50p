amt = 50

while amt > 0:
    print("Amount Due:", amt)
    coin = int(input("Insert Coin: "))
    if coin not in [25, 10, 5]:
        continue
    amt -= coin

print("Change Owed:", -amt)
