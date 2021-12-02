
from validation.validation import Validation

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
    
    def test_handler(self):
        self.test_validate_base()
        self.test_validate_number()
        self.test_validate_rapid_base()


if __name__ == "__main__":

    validation_test = ValidationTest()
    validation_test.test_handler()
