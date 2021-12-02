

class Validation:

    def __init__(self):
        pass
    
    @staticmethod
    def validate_base(base):
        err = ""
        try:
            base = int(base)
            if base < 2 or base > 16:
                err += "Base has to be between 2 and 16!"
        except ValueError as ve:
            raise ValueError("Base must be a number!")
        if len(err):
            raise ValueError(err)
    
    @staticmethod
    def validate_number(base, number):
        base = int(base)
        number = number.lower()
        digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        digit_list = digit_list[:base]
        bad_digits = list()
        for digit in number:
            if not digit in digit_list:
                bad_digits.append(digit)
        if len(bad_digits):
            raise ValueError(f"The digits {bad_digits} are not in base {base}!") # {i for i in bad_digits}
    
    @staticmethod
    def validate_rapid_base(base):
        err = ""
        try:
            base = int(base)
            if not (base == 2 or base == 4 or base == 8 or base == 16):
                err += "Base must be 2, 4, 8 or 16!"
        except ValueError as ve:
            raise ValueError("Base must be a number!")
        if len(err):
            raise ValueError(err)