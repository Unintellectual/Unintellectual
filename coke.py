coke = 50

while coke > 0:
    print(f"Amount Due: {coke}" )
    Input = int(input("Insert Coin: "))

    if Input in [50, 25, 10, 5]:
        coke -= Input
        print(Input, end="")
