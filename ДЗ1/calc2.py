def summa(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


n1 = int(input("Введите 1 число: "))
n2 = int(input("Введите 2 число: "))
z = input("Введите знак: ")
if z == "+":
    print(summa(n1, n2))
elif z == '-':
    print(substract(n1, n2))
elif z == "*":
    print(multiply(n1, n2))
elif z == "/" and n2 != 0:
    print(divide(n1, n2))
elif z == "/" and n2 == 0:
    print("На 0 делить нельзя")