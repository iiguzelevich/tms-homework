from exception import CustomError1
from exception import CustomError2


class Calculator:
    """Calculator"""

    def __init__(self):
        self.exit = None
        self.ce = None
        self.calculator_string = None
        self.action = None
        self.number_1 = None
        self.number_2 = None
        self.result = None

    @staticmethod
    def information():
        """shows the available operations with the calculator"""

        print(
            'available actions:\n'
            'sum: +\n'
            'subtract: -\n'
            'multiply: *\n'
            'divided: /\n'
            'example: "number 1" "action" "number 2"\n\n'
            'exit: off\n'
        )

    @staticmethod
    def information_to_continue():
        """shows the available operations with the calculator"""

        print(
            'available actions:\n'
            'sum: +\n'
            'subtract: -\n'
            'multiply: *\n'
            'divided: /\n'
            'exponentiation: ^\n'
            'example: "action" "number 2"\n\n'
            'clear the calculator line: ce\n'
            'exit: off\n'
        )

    def initializing_string(self):
        """initializing numbers and actions"""

        self.calculator_string = (input("enter what you want to count: "))

        if self.calculator_string == 'off':
            self.exit = 'off'
            return 'off'

        try:
            if len(self.calculator_string.split(' ')) > 3:
                raise CustomError1('invalid input')

            self.number_1 = float(self.calculator_string.split(' ')[0])
            self.number_2 = float(self.calculator_string.split(' ')[2])

            self.action = self.calculator_string.split(' ')[1]
            if (self.action != '/'
                    and self.action != '*'
                    and self.action != '+'
                    and self.action != '-'
                    and self.action != '^'):
                raise CustomError2('incorrect input of an arithmetic action')

        except IndexError:
            print('Please enter as in the example')
            return self.initializing_string()

        except ValueError:
            print('Please enter the correct values')
            return self.initializing_string()

        except CustomError1:
            print('Please enter only two numbers and action')
            return self.initializing_string()

        except CustomError2:
            print('Please enter the correct arithmetic action')
            return self.initializing_string()

        return self.number_1, self.action, self.number_2

    def applying_actions(self):
        """performs actions with numbers depending on user input"""

        if self.action == '*':
            self.result = self.number_1 * self.number_2
            return self.result

        elif self.action == '+':
            self.result = self.number_1 + self.number_2
            return self.result

        elif self.action == '/':
            try:
                self.result = self.number_1 / self.number_2

            except ZeroDivisionError:
                self.result = 0
                return self.result

            return self.result

        elif self.action == '-':
            self.result = self.number_1 - self.number_2
            return self.result

        elif self.action == '^':
            self.result = self.number_1 ** self.number_2
            return self.result

    def continue_computing(self):
        """
        initializing the result after the first action,
        the second number and the action
        """

        self.calculator_string = input(f'{self.result} ')

        if self.calculator_string.strip() == 'off':
            self.exit = 'off'
            return self.exit

        elif self.calculator_string.strip() == 'ce':
            self.ce = 'ce'
            return self.ce

        else:
            try:
                if len(self.calculator_string.split()) > 2:
                    raise CustomError1
                self.number_1 = float(self.result)
                self.number_2 = float(self.calculator_string.split(' ')[1])
                self.action = self.calculator_string.split(' ')[0]
                if (self.action != '/'
                        and self.action != '*'
                        and self.action != '+'
                        and self.action != '-'
                        and self.action != '^'):
                    raise CustomError2

            except IndexError:
                print('Please enter as in the example')
                return self.initializing_string()

            except ValueError:
                print('Please enter the correct values')
                return self.initializing_string()

            except TypeError:
                print('Please enter as in the example')
                return self.initializing_string()

            except CustomError1:
                print('Please enter only the action and the number')
                return self.initializing_string()

            except CustomError2:
                print('Please enter the correct action')
                return self.initializing_string()

    def update_exit_and_ce(self):
        """updating variables to exit or clear a row after an action"""

        self.exit = None
        self.ce = None
        return self.exit, self.ce

    def order_of_commands(self):
        """
        the order of commands for the correct operation
        of the calculator
        """

        while True:
            if self.exit is not None:
                break
            self.information()

            self.initializing_string()

            if self.exit is not None:
                break

            while True:

                self.information_to_continue()
                self.update_exit_and_ce()
                self.applying_actions()
                self.continue_computing()

                if self.ce is not None:
                    break

                elif self.exit is not None:
                    break


my_calculator = Calculator()
my_calculator.order_of_commands()


