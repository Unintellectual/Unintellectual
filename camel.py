Input = input("camelCase: ")
print("snake_case: ", end="")

for letters in Input:
    if letters.isupper():
        print("_" + letters.lower(), end="")
    else:
        print(letters, end="")
print()
