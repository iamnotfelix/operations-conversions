
from validation.validation import Validation

class ValidationTest:

    def __init__(self) -> None:
        self.validator = Validation()

    def test_validate_base(self):
        pass

    def test_validate_number(self):
        pass

    def test_validate_rapid_base(self):
        pass
    
    def test_handler(self):
        self.test_validate_base()
        self.test_validate_number()
        self.test_validate_rapid_base()


if __name__ == "__main__":

    validation_test = ValidationTest()
    validation_test.test_handler()
