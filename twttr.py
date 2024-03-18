def shorten():
    Input = input("Input: ")
    print("Output: ", end="")
    for letter in Input:
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O" , "U" ]

    if not letter in vowels:
        print(letter, end="")

print()
