
from domain.number import Number
from services.operations import Operations
from validation.validation import Validation


class NumberTest:
    
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def test_create_digit_list():
        number = Number("12", "AB123")
        assert number.digit_list == [3, 2, 1, 11, 10]

        number = Number("16", "FABCDE12")
        assert number.digit_list == [2, 1, 14, 13, 12, 11, 10, 15]
    
    def test_create_value(self):
        number = Number("12", "ABc123")
        assert number.create_value(number.digit_list) == "ABC123"

        number = Number("16", "FABCDE12")
        assert number.create_value(number.digit_list) == "FABCDE12"

    def test_handler(self):
        self.test_create_digit_list()
        self.test_create_value()

class ValidationTest:

    def __init__(self) -> None:
        self.validator = Validation()

    def test_validate_base(self):
        try:
            self.validator.validate_base("afd")
            assert False
        except ValueError as ve:
            assert str(ve) == "Base must be a number!"
        
        try:
            self.validator.validate_base("17")
            assert False
        except ValueError as ve:
            assert str(ve) == "Base has to be between 2 and 16!"

        try:
            self.validator.validate_base("1")
            assert False
        except ValueError as ve:
            assert str(ve) == "Base has to be between 2 and 16!"

    def test_validate_number(self):
        try:
            self.validator.validate_number("2", "12")
            assert False
        except ValueError as ve:
            assert str(ve) == "The digits ['2'] are not in base 2!"

        try:
            self.validator.validate_number("10", "123456Abc")
            assert False
        except ValueError as ve:
            assert str(ve) == "The digits ['a', 'b', 'c'] are not in base 10!"

    def test_validate_rapid_base(self):
        try:
            self.validator.validate_rapid_base("afdfh")
            assert False
        except ValueError as ve:
            assert str(ve) == "Base must be a number!"
        
        try:
            self.validator.validate_rapid_base("10")
            assert False
        except ValueError as ve:
            assert str(ve) == "Base must be 2, 4, 8 or 16!"

        try:
            self.validator.validate_rapid_base("3")
            assert False
        except ValueError as ve:
            assert str(ve) == "Base must be 2, 4, 8 or 16!"
    
    def tests_handler(self):
        self.test_validate_base()
        self.test_validate_number()
        self.test_validate_rapid_base()


class OperationsTest:

    def __init__(self) -> None:
        self.operations = Operations()

    def test_add(self):
        assert self.operations.add(16, "abcde", "123456") == "1CF134"
        assert self.operations.add(7, "123432", "654324") == "1111056"
        assert self.operations.add(2, "11001100", "110011") == "11111111"
        assert self.operations.add(6, "23045", "100254") == "123343"
        assert self.operations.add(2, "11100111001110101", "1101111011111") == "11110101001010100"
        assert self.operations.add(16, "ABCDE", "D9037F") == "E3C05D"
        assert self.operations.add(12, "Ab23", "A45") == "B968"

    def test_substract(self):
        assert self.operations.substract(2, "10001100010", "1110111011") == "10100111" 
        assert self.operations.substract(9, "102387", "64502") == "26785"
        assert self.operations.substract(16, "501BA", "32Ed") == "4CECD"
        assert self.operations.substract(8, "130046", "71257") == "36567" 
        assert self.operations.substract(7, "210354", "55466") == "121555"
        assert self.operations.substract(12, "Ab23", "A45") == "A09A"

    def test_multiply(self):
        assert self.operations.multiply(8, "7023", "5") == "43137"
        assert self.operations.multiply(16, "32001b", "6") == "12C00A2"
        assert self.operations.multiply(7, "12345", "5") == "65424"
        assert self.operations.multiply(6, "12345", "5") == "111101"
        assert self.operations.multiply(5, "31203", "3") == "144114"
        assert self.operations.multiply(4, "31203", "3") == "220221"

    def test_divide(self):
        assert self.operations.divide(3, "20101", "2") == "10012    r: 0"
        assert self.operations.divide(16, "1fed0205", "9") == "38C1CAB    r: 2"
        assert self.operations.divide(8, "120456", "6") == "15335    r: 0"
        assert self.operations.divide(7, "120456", "6") == "13421    r: 0"
        assert self.operations.divide(5, "321023", "3") == "103322    r: 2"
        assert self.operations.divide(4, "321023", "3") == "103003    r: 2"

    def tests_handler(self):
        self.test_add()
        self.test_substract()
        self.test_multiply()
        self.test_divide()


if __name__ == "__main__":

    number_test = NumberTest()
    validation_test = ValidationTest()
    operations_test = OperationsTest()

    number_test.test_handler()
    validation_test.tests_handler()
    operations_test.tests_handler()
