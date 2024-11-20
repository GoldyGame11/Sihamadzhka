class Calculator:
    def __init__(self):
        pass

    def str_to_float(self, value):
        try:
            result = float(value)
            print(f"Conversion '{value}' successful.")
            return result
        except ValueError:
            print("Error.")
            return None

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            print("Error")
            return None
        return a / b


calc = Calculator()

num1 = calc.str_to_float("10")
num2 = calc.str_to_float("abc")

if num1 is not None:
    print("+:", calc.add(num1, 10))
    print("-:", calc.subtract(num1, 20))
    print("*:", calc.multiply(num1, 3))
    result = calc.divide(num1, 0)
    if result is not None:
        print("::", result)
