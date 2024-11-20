class Calculation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def umnozit(self):
        return self.a * self.b

    def dilit(self):
        return self.a / self.b

    def minus(self):
        return self.a - self.b

    def plusil(self):
        return self.a + self.b


a = 1488
b = 52
calc = Calculation(a, b)

print("Умножение:", calc.umnozit())
print("Деление:", calc.dilit())
print("Отнемание:", calc.minus())
print("Add:", calc.plusil())




