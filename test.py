
from domain.number import Number
from services.conversions import Conversions
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
    
    @staticmethod
    def test_eq():
        number = Number("12", "AB123") 
        assert number.__eq__(Number("12", "AB123"))

        number = Number("16", "FABCDE12")
        assert number.__eq__(Number("16", "FABCDE12"))

    @staticmethod
    def test_greater():
        num1 = Number("10", "1234")
        num2 = Number("10", "123")

        assert Number.greater(num1, num2)
        assert not Number.greater(num2, num1)

        num2 = Number("10", "1234")
        assert not Number.greater(num1, num2)
        assert not Number.greater(num2, num1)

        num2 = Number("10", "1235")
        assert Number.greater(num2, num1)
        assert not Number.greater(num1, num2)

        num1 = Number("10", "1400")
        assert Number.greater(num1, num2)
        assert not Number.greater(num2, num1)
    
    @staticmethod
    def test_create_value():
        number = Number("12", "ABc123")
        assert number.create_value(number.digit_list) == "ABC123"

        number = Number("16", "FABCDE12")
        assert number.create_value(number.digit_list) == "FABCDE12"

    @staticmethod
    def test_split_in_chunks():
        number = Number("2", "100010011010100101")
        assert number.split_in_chunks(4) == ["0101", "1010", "0110", "0010","10"]
        assert number.split_in_chunks(3) == ["101", "100", "010", "011","010", "100"]
        assert number.split_in_chunks(2) == ["01", "01", "10", "10", "10", "01", "10", "00", "10"]

    def test_handler(self):
        self.test_create_digit_list()
        self.test_eq()
        self.test_create_value()
        self.test_greater()
        self.test_split_in_chunks()

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
            assert str(ve) == "Base has to be between 2 and 10 or 16!"

        try:
            self.validator.validate_base("1")
            assert False
        except ValueError as ve:
            assert str(ve) == "Base has to be between 2 and 10 or 16!"

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
        assert self.operations.add(16, "abcde", "123456").value == "1CF134"
        assert self.operations.add(7, "123432", "654324").value == "1111056"
        assert self.operations.add(2, "11001100", "110011").value == "11111111"
        assert self.operations.add(6, "23045", "100254").value == "123343"
        assert self.operations.add(2, "11100111001110101", "1101111011111").value == "11110101001010100"
        assert self.operations.add(16, "ABCDE", "D9037F").value == "E3C05D"
        assert self.operations.add(12, "Ab23", "A45").value == "B968"

    def test_substract(self):
        try:
            self.operations.substract(10, "100", "101")
            assert False
        except Exception as ex:
            assert str(ex) == "X has to be greater or equal than Y!"

        assert self.operations.substract(2, "10001100010", "1110111011").value == "10100111" 
        assert self.operations.substract(9, "102387", "64502").value == "26785"
        assert self.operations.substract(16, "501BA", "32Ed").value == "4CECD"
        assert self.operations.substract(8, "130046", "71257").value == "36567" 
        assert self.operations.substract(7, "210354", "55466").value == "121555"
        assert self.operations.substract(12, "Ab23", "A45").value == "A09A"

    def test_multiply(self):
        assert self.operations.multiply(8, "7023", "5").value == "43137"
        assert self.operations.multiply(16, "32001b", "6").value == "12C00A2"
        assert self.operations.multiply(7, "12345", "5").value == "65424"
        assert self.operations.multiply(6, "12345", "5").value == "111101"
        assert self.operations.multiply(5, "31203", "3").value == "144114"
        assert self.operations.multiply(4, "31203", "3").value == "220221"

    def test_divide(self):
        try:
            self.operations.divide(8, "1234", "0")
            assert False
        except Exception as ex:
            assert str(ex) == "Can not divide by 0!"

        result, remainder = self.operations.divide(3, "20101", "2")
        assert  result.__eq__(Number(3, "10012"))
        assert remainder == 0

        result, remainder = self.operations.divide(16, "1fed0205", "9")
        assert result.__eq__(Number(16, "38C1CAB"))
        assert remainder == 2

        result, remainder = self.operations.divide(8, "120456", "6")
        assert result.__eq__(Number(8, "15335"))
        assert remainder == 0

        result, remainder = self.operations.divide(7, "120456", "6")
        assert result.__eq__(Number(7, "13421"))
        assert remainder == 0

        result, remainder = self.operations.divide(5, "321023", "3")
        assert result.__eq__(Number(5, "103322"))
        assert remainder == 2

        result, remainder = self.operations.divide(4, "321023", "3")
        assert result.__eq__(Number(4, "103003"))
        assert remainder == 2

    def tests_handler(self):
        self.test_add()
        self.test_substract()
        self.test_multiply()
        self.test_divide()


class ConversionsTest:

    def __init__(self) -> None:
        self.operations = Operations()
        self.conversions = Conversions(self.operations)

    def test_successive_division_method(self):
        try:
            self.conversions.successive_division_method("2","1001010","8")
            assert False
        except Exception as ex:
            assert str(ex) == "For the successive division method the source base must be greater than the destination base!"

        assert self.conversions.successive_division_method("8", "11024", "2") == "1001000010100"
        assert self.conversions.successive_division_method("16", "BCF13F", "2") == "101111001111000100111111"
        assert self.conversions.successive_division_method("2", "10000001101100", "2") == "10000001101100"
        assert self.conversions.successive_division_method("13", "ABc12", "5") == "34434240"
        assert self.conversions.successive_division_method("14", "ABc12", "4") == "1211233020"

    def test_substitution_method(self):
        try:
            self.conversions.substitution_method("8", "11234","2")
            assert False
        except Exception as ex:
            assert str(ex) == "For the substitution method the source base must be lower than the destination base!"
        assert self.conversions.substitution_method("2", "10000001101100", "8") == "20154"
        assert self.conversions.substitution_method("4", "3210", "9") == "273"
        assert self.conversions.substitution_method("5", "1234", "16") == "C2"
        assert self.conversions.substitution_method("7", "16663", "10") == "4798"
        assert self.conversions.substitution_method("2", "1100100100011000101", "10") == "411845"
        assert self.conversions.substitution_method("6", "1100100100011000101", "10") == "118565343400933"
        assert self.conversions.substitution_method("2", "1100100100011000101", "6") == "12454405"

    def test_intermediate_base_method(self):
        pass

    def test_rapid_conversion_method(self):
        assert self.conversions.rapid_conversion_method("8","1234567", "16") == "53977"
        assert self.conversions.rapid_conversion_method("16","abc123fd", "8") == "25360221775"
        assert self.conversions.rapid_conversion_method("2", "10000001101100", "2") == "10000001101100"
        assert self.conversions.rapid_conversion_method("2", "10000001101100", "4") == "2001230"
        assert self.conversions.rapid_conversion_method("4", "32112311123123312313133212311231", "16") == "E5B56DBDB77E6D6D"

    def test_handler(self):
        self.test_successive_division_method()
        self.test_substitution_method()
        self.test_intermediate_base_method()
        self.test_rapid_conversion_method()

if __name__ == "__main__":

    number_test = NumberTest()
    validation_test = ValidationTest()
    operations_test = OperationsTest()
    conversions_test = ConversionsTest()

    number_test.test_handler()
    validation_test.tests_handler()
    operations_test.tests_handler()
    conversions_test.test_handler()


# todo: when converting from base ten or to base ten, there are error because of the multiplication or division by 10 (more than one digit)
