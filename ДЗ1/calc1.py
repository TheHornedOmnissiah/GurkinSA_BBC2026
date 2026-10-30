n1 = int(input("Введите 1 число: "))
n2 = int(input("Введите 2 число: "))
z = input("Введите знак: ")
if z == "+":
    print(n1 + n2)
elif z == '-':
    print(n1 - n2)
elif z == "*":
    print(n1 * n2)
elif z == "/" and n2 != 0:
    print(n1 / n2)
elif z == "/" and n2 == 0:
    print("На 0 делить нельзя")