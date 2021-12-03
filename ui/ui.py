

from services.conversions import Conversions


class UI:
    def __init__(self, conversions, operations, validator):
        self.__conversions = conversions
        self.__operations = operations
        self.__validator = validator

    """
        Menus
    """

    @staticmethod
    def print_main_menu():
        print("\nEnter a command:")
        print("conversions\tGo to conversions menu.")
        print("operations\tGo to operations menu.")
        print("\nexit\tExit the application.\n")

    @staticmethod
    def print_conversions_menu():
        print("\nEnter one command:")
        print("1\tConvert using succesive division method.")
        print("2\tConvert using substitution method.")
        print("3\tConvert using 10 as intermediate base.")
        print("4\tConvert using rapid conversions(only between bases: 2, 4, 8, 16).")
        print("\nhelp\tDisplay this menu.")
        print("back\tGo back to main menu.")
        print("exit\tExit the application.\n")

    @staticmethod
    def print_operations_menu():
        print("\nEnter a command:")
        print("add\tAdd two numbers.")
        print("sub\tSubstract two numbers.")
        print("mul\tMultiply two numbers(multiply by one digit).")      
        print("div\tDivide two numbers(divide by one digit).")
        print("\nhelp\tDisplay this menu.")
        print("back\tGo back to main menu.")
        print("exit\tExit the application.\n")


    """
        Utility functions
    """

    @staticmethod
    def get_command():
        command = input(">>>")
        command = command.strip()
        return command

    def get_conversion_input(self):
        source_base = input("Enter the source base: ")
        self.__validator.validate_base(source_base)

        number = input("Enter the number: ")
        self.__validator.validate_number(source_base, number)

        destination_base = input("Enter the destination base: ")
        self.__validator.validate_base(destination_base)

        return source_base, number, destination_base

    def get_rapid_conversion_input(self):
        source_base = input("Enter the source base: ")
        self.__validator.validate_rapid_base(source_base)

        number = input("Enter the number: ")
        self.__validator.validate_number(source_base, number)

        destination_base = input("Enter the destination base: ")
        self.__validator.validte_rapid_base(destination_base)

        return source_base, number, destination_base
    
    def get_operation_input(self):
        base = input("Enter the base: ")
        self.__validator.validate_base(base)

        num1 = input(f"Enter a value for x: ")
        self.__validator.validate_number(base, num1)

        num2 = input(f"Enter a value for y: ")
        self.__validator.validate_number(base, num2)

        return base, num1, num2

    def operation(self, operator, operation_func):
        print(f"x {operator} y = ?")
        data = self.get_operation_input()
        result = operation_func(*data)
        if isinstance(result, tuple):
            result, borrow = result[0], result[1]
            print(f"{data[1]} {operator} {data[2]} = {result.value}    r: {borrow}")
        else:
            print(f"{data[1]} {operator} {data[2]} = {result.value}")

    """
        Menu handlers
    """

    def main_command_handler(self):
        command = self.get_command()
        try:
            if command == "exit":
                exit()
            elif command == "help":
                self.print_main_menu()
            elif command == "conversions":
                self.conversions_command_handler()
            elif command == "operations":
                self.operations_command_handler()
            else:
                raise Exception("Invalid command!")
        except Exception as ex:
            print(str(ex))
    
    def conversions_command_handler(self):
        self.print_conversions_menu()
        while True:
            command = self.get_command()
            try:
                if command == "back":
                    return
                elif command == "exit":
                    exit()
                elif command == "help":
                    self.print_conversions_menu()
                elif command == "1":    # Successive division method
                    data = self.get_conversion_input()
                    print(self.__conversions.successive_division_method(*data))
                elif command == "2":    # Substitutoin method
                    data = self.get_conversion_input()
                    print(self.__conversions.substitution_method(*data))
                elif command == "3":    # 10 as intermediate base
                    data - self.get_conversion_input()
                    print(self.__conversions.intermediate_base_method(*data))
                elif command == "4":    # Rapid conversion method
                    data = self.get_rapid_conversion_input()
                    print(self.__conversions.rapid_conversion_method(*data))
                else:
                    raise Exception("Invalid command!")
            except Exception as ex:
                print(str(ex))

    def operations_command_handler(self):
        self.print_operations_menu()
        while True:
            command = self.get_command()
            try:
                if command == "back":
                    return
                elif command == "exit":
                    exit()
                elif command == "help":
                    self.print_operations_menu()
                elif command == "add":
                    self.operation("+", self.__operations.add)
                elif command == "sub":
                    self.operation("-", self.__operations.substract)
                elif command == "mul":
                    self.operation("*", self.__operations.multiply)
                elif command == "div":
                    self.operation("/", self.__operations.divide)
                else:
                    raise Exception("Invalid command!")
            except Exception as ex:
                print(str(ex))


    """
        Main function
    """

    def start(self):
        self.print_main_menu()
        while True:
            self.main_command_handler()

# todo: provide in the menu the bases that can be used and other info
