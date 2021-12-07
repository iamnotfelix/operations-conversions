
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
        
        value = Number.create_value(result)
        result = Number(base, value)
        return result

    def substract(self, base, num1, num2):
        borrow = 0
        base = int(base)
        num1 = Number(base, num1)
        num2 = Number(base, num2)
        result = list()

        if Number.greater(num2, num1):
            raise Exception("X has to be greater or equal than Y!")

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
        
        result = Number.create_value(result)
        result = Number(base, result)
        return result

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

        if len(num2) > 1:
            raise Exception("Can only multiply with a digit!")

        for index in range(0, len(num1)):
            mul = carry + num1[index] * num2[0]
            carry = mul // base
            result.append(mul % base)

        if carry:
            result.append(carry)
        
        result = Number.create_value(result)
        result = Number(base, result)
        return result

    def divide(self, base, num1, num2):
        borrow = 0
        base = int(base)
        num1 = Number(base, num1)
        num2 = Number(base, num2)
        result = list()

        if num2.value == "0":
            raise Exception("Can not divide by 0!")
        
        if len(num2) > 1:
            raise Exception("Can only divide by a digit!")

        for index in reversed(range(0, len(num1))):
            div = borrow * base + num1[index]
            borrow = div % num2[0]
            result.append(div // num2[0])

        result = Number.create_value(result, False)
        result = Number(base, result)
        return result, borrow
        # return f"{Number.create_value(result, False)}    r: {borrow}"
