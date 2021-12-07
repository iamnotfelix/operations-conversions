

from domain.number import Number
from math import log2


class Conversions:
    def __init__(self, operations):
        self.__operations = operations

    def successive_division_method(self, source_base, number, destination_base):
        if int(destination_base) > int(source_base):
            raise Exception("For the successive division method the source base must be greater than the destination base!")

        number = Number(source_base, number)
        result = list()

        if destination_base == "10":
            destination_base = "A"

        while number.value != "0":
            number, remainder = self.__operations.divide(number.base, number.value, destination_base)
            result.append(remainder)
        
        return Number.create_value(result)

    def substitution_method(self, source_base, number, destination_base):
        if int(destination_base) < int(source_base):
            raise Exception("For the substitution method the source base must be lower than the destination base!")

        number = Number(source_base, number)
        result = "0"

        if source_base == "10":
            source_base = "A"

        for i in range(0, len(number)):
            base_multiplier = "1"
            for j in range(0, i):
                base_multiplier = self.__operations.multiply(destination_base, base_multiplier, source_base)
                base_multiplier = base_multiplier.value

            sum = self.__operations.multiply(destination_base, base_multiplier, str(number[i]))
            sum = sum.value

            result = self.__operations.add(destination_base, sum, result)
            result = result.value
        
        return result

    def intermediate_base_method(self, source_base, number, destination_base):
        result = number
        if int(source_base) > 10:
            result = self.successive_division_method(source_base, number, "10")
        elif int(source_base) < 10:
            result = self.substitution_method(source_base, number, "10")

        if int(destination_base) > 10:
            result = self.substitution_method("10", result, destination_base)
        elif int(destination_base) < 10:
            result = self.successive_division_method("10", result, destination_base)
        
        return result

    def rapid_conversion_method(self, source_base, number, destination_base):
        base_2 = { "0000": "0", "0001": "1", "0010": "2", "0011": "3", "0100": "4", "0101": "5", "0110": "6", "0111": "7", 
                "1000": "8", "1001": "9", "1010": "A", "1011": "B", "1100": "C", "1101": "D", "1110": "E", "1111": "F" }

        to_base_2 = { "0": "0", "1": "1", "2": "10", "3": "11", "4": "100", "5": "101", "6": "110", "7": "111",
                 "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111" }

        in_base_2 = ""
        chunk_size = int(log2(int(source_base)))
        for digit in number:
            chunk = to_base_2[digit.upper()]
            chunk = "0" * (chunk_size - len(chunk)) + chunk
            in_base_2 += chunk

        chunk_size = int(log2(int(destination_base)))
        number = Number(source_base, in_base_2)
        chunks = number.split_in_chunks(chunk_size)

        for i in range(0, len(chunks)):
            chunks[i] = "0" * (4 - len(chunks[i])) + chunks[i]

        result = ""
        for chunk in chunks:
            result += base_2[chunk]
        
        result = result[::-1]
        result = result.lstrip("0")
        return result
