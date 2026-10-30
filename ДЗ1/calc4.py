class Calc:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def summa(self):
        return self.n1 + self.n2

    def substract(self):
        return self.n1 - self.n2

    def multiply(self):
        return self.n1 * self.n2

    def divide(self):
        return self.n1 / self.n2


n1 = int(input("Введите 1 число: "))
n2 = int(input("Введите 2 число: "))
digits = Calc(n1, n2)

print(digits.summa())
