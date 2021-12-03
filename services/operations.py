
from domain.number import Number


class Operations:

    def __init__(self):
        pass

    def add(self, base, num1, num2):
        carry = 0
        base = int(base)
        num1 = Number(base, num1)
        num2 = Number(base, num2)
        result = list()

        if len(num1) > len(num2):
            num2.extend_number(abs(len(num1) - len(num2)))
        else:
            num1.extend_number(abs(len(num1) - len(num2)))

        for index in range(0, len(num1)):
            sum = num1[index] + num2[index] + carry
            carry = sum // base
            result.append(sum % base)

        if carry:
            result.append(carry)
        
        return Number.create_value(result)

    def substract(self, base, num1, num2):
        borrow = 0
        base = int(base)
        num1 = Number(base, num1)
        num2 = Number(base, num2)
        result = list()

        if len(num2) < len(num1):
            num2.extend_number(abs(len(num2) - len(num1)))

        for index in range(0, len(num1)):
            sub = num1[index] - num2[index] + borrow
            if sub < 0:
                borrow = -1
                result.append(base + sub)
            else:
                borrow = 0
                result.append(sub)
        
        return Number.create_value(result)


    def multiply(self, base, num1, num2):
        carry = 0
        base = int(base)
        num1 = Number(base, num1)
        num2 = Number(base, num2)
        result = list()

        if len(num1) < len(num2):
            aux = num1
            num1 = num2
            num2 = aux

        for index in range(0, len(num1)):
            mul = carry + num1[index] * num2[0]
            carry = mul // base
            result.append(mul % base)

        if carry:
            result.append(carry)
        
        return Number.create_value(result)

    def divide(self, base, num1, num2):
        borrow = 0
        base = int(base)
        num1 = Number(base, num1)
        num2 = Number(base, num2)
        result = list()

        for index in reversed(range(0, len(num1))):
            div = borrow * base + num1[index]
            borrow = div % num2[0]
            result.append(div // num2[0])

        return f"{Number.create_value(result, False)}    r: {borrow}"

# todo: make a validation for substraction that ensures that the second number is smaller than the first one?