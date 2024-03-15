amountDue = 50

while amountDue > 0:
    print(f"Amount Due: {amountDue}" )
    Input = int(input("Insert Coin: "))

    if Input in [25, 10, 5]:
        amountDue-= Input
        print(Input, end="")
