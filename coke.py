amountDue = 50

while amountDue > 0:
    print(f"Amount Due: {amountDue}" )
    coin = int(input("Insert Coin: "))

    if  coin in [25, 10, 5]:
        amountDue -= coin


changeOwed = abs(amountDue)

print("Change Owed: ", changeOwed)
