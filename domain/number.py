

class Number:

    def __init__(self, base, value) -> None:
        self.__base = base
        self.__value = value
        self.__list_value = list()

    @property
    def base(self):
        return self.__base

    @property
    def value(self):
        return self.__value
    
    @property
    def list_value(self):
        return self.__list_value

    def create_list_value(self):
        pass
