

class Number:

    def __init__(self, base, value) -> None:
        self.__base = base
        self.__value = value.lower()
        self.__digit_list = self.create_digit_list()

    @property
    def base(self):
        return self.__base

    @property
    def value(self):
        return self.__value
    
    @property
    def digit_list(self):
        return self.__digit_list

    def __len__(self):
        return len(self.__digit_list)
    
    def __getitem__(self, i):
        return self.digit_list[i]

    def create_digit_list(self):
        self.__value = self.__value.lower()
        digit_list = list()
        for digit in reversed(self.__value):
            try:
                digit = int(digit)
            except ValueError:
                digit = ord(digit) - 87         # ascii code o a lowercase letter - 87 = value in base 10
            digit_list.append(digit)
        return digit_list

    def extend_number(self, nr_digits):
        for i in range(nr_digits):
            self.__digit_list.append(0)

    @staticmethod
    def create_value(digit_list, dir=True):
        value = ""
        if dir:
            digit_list = reversed(digit_list)
        for digit in digit_list:
            if digit > 9:
                value += chr(digit + 87)
            else:
                value += str(digit)
        value = value.lstrip('0')
        return value.upper()



if __name__ == "__main__":
    number = Number(16, "ABCDEF123")
    print(number.digit_list)