

from domain.number import Number


class Conversions:
    def __init__(self, operations):
        self.__operations = operations

    def successive_division_method(self, source_base, number, destination_base):
        if int(destination_base) > int(source_base):
            raise Exception("For the successive division method the source base must be greater than the destination base!")

        number = Number(source_base, number)
        result = list()

        while number.value != "0":
            number, remainder = self.__operations.divide(number.base, number.value, destination_base)
            result.append(remainder)
        
        return Number.create_value(result)

    def substitution_method(self, source_base, number, destination_base):
        if int(destination_base) < int(source_base):
            raise Exception("For the substitution method the source base must be lower than the destination base!")

        number = Number(source_base, number)
        result = "0"
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
        pass

    def rapid_conversion_method(self, source_base, number, destination_base):
        pass

# todo: source_base has to be lower than the destination base for successive division
# the successive_division does not work with two bases that are both over 10. so i need to implement that?
# no!!!!
# conversions of natural numbers between two bases p,q{2,3,...,9,10,16} using the substitution method 
#                   or successive divisions and rapid conversions between two bases p,q{2, 4, 8, 16}.