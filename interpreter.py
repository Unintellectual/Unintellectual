expression = input("Expression: ")
x, y, z = expression.split(" ")

newX = float(x)
newZ = float(z)

if y == "+":
    result = newX + newZ
if y == "-":
    result = newX - newZ
if y == "*":
    result = newX * newZ
if y == "/":
    result = newX / newZ


print(result)

