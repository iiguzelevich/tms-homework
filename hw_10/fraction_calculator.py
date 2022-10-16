from exception import CustomError1
from exception import CustomError2


class Calculator:
    """fraction calculator"""

    def __init__(self):
        self.result_denominator = None
        self.result_numerator = None
        self.denominator_2 = None
        self.denominator_1 = None
        self.numerator_2 = None
        self.numerator_1 = None
        self.action = None

    @staticmethod
    def information():
        """shows the available operations with the calculator"""

        print(
            'available functions:\n'
            'sum: +\n'
            'subtract: -\n'
            'multiply: *\n'
            'divided: /\n'
            'exit: off\n'
        )

    def initialization(self):
        """initializing numbers and actions"""
        try:
            self.numerator_1 = (
                input("enter the numerator for the first number: "))
            if self.numerator_1 == 'off':
                return 'off'
            self.numerator_1 = int(self.numerator_1)

            self.denominator_1 = (
                input("enter the denominator for the first number: "))
            if self.denominator_1 == 'off':
                return 'off'
            self.denominator_1 = int(self.denominator_1)

            self.action = (input("enter action: "))
            if self.action == 'off':
                return 'off'

            elif (self.action != '/'
                  and self.action != '*'
                  and self.action != '+'
                  and self.action != '-'):
                raise CustomError1('incorrect input of an arithmetic action')

            self.numerator_2 = (
                input("enter the numerator for the second number: "))
            if self.numerator_2 == 'off':
                return 'off'
            self.numerator_2 = int(self.numerator_2)

            self.denominator_2 = (
                input("enter the denominator for the second number: "))
            if self.denominator_2 == 'off':
                return 'off'
            self.denominator_2 = int(self.denominator_2)

            if ((self.numerator_2 == 0 and self.action == '/')
                    or (self.denominator_2 == 0 or self.denominator_1 == 0)):
                raise CustomError2('Division by zero')

            if (self.action != '/'
                    and self.action != '*'
                    and self.action != '+'
                    and self.action != '-'
                    and self.action != '^'):
                raise CustomError1('incorrect input of an arithmetic action')

        except ValueError:
            print('Please enter the correct values')
            return self.initialization()

        except CustomError1:
            print('Please enter the correct arithmetic action')
            return self.initialization()

        except CustomError2:
            print('Division by zero')
            return self.initialization()

    def func_nod(self, x, y):
        """factorial for finding the greatest common divisor"""

        if y == 0:
            return x
        else:
            return self.func_nod(y, x % y)

    def applying_actions(self):
        """performs actions with numbers depending on user input"""

        if self.action == '*':
            result_numerator = self.numerator_1 * self.numerator_2
            result_denominator = self.denominator_1 * self.denominator_2
            nod = self.func_nod(result_numerator, result_denominator)

            self.result_numerator = int(result_numerator / nod)
            self.result_denominator = int(result_denominator / nod)
            return self.result_numerator, self.result_denominator

        elif self.action == '/':
            result_numerator = self.numerator_1 * self.denominator_2
            result_denominator = self.denominator_1 * self.numerator_2

            nod = self.func_nod(result_numerator, result_denominator)

            self.result_numerator = int(result_numerator / nod)
            self.result_denominator = int(result_denominator / nod)

            return self.result_numerator, self.result_denominator

        elif self.action == '+':
            result_numerator = (
                    self.numerator_1 * self.denominator_2
                    + self.denominator_1 * self.numerator_2
            )

            result_denominator = self.denominator_1 * self.denominator_2

            nod = self.func_nod(result_numerator, result_denominator)

            self.result_numerator = int(result_numerator / nod)
            self.result_denominator = int(result_denominator / nod)

            return self.result_numerator, self.result_denominator

        elif self.action == '-':
            result_numerator = (
                    self.numerator_1 * self.denominator_2
                    - self.denominator_1 * self.numerator_2
            )

            result_denominator = self.denominator_1 * self.denominator_2

            nod = self.func_nod(result_numerator, result_denominator)

            self.result_numerator = int(result_numerator / nod)
            self.result_denominator = int(result_denominator / nod)

            return self.result_numerator, self.result_denominator

    def show_result(self):
        """result output"""

        if self.result_numerator == 0:
            self.result_denominator = 0
            shape = (
                """
                {n_1}      {n_2}      
                --  {action}  --  =   0
                {d_1}      {d_2}       
                """
            )
            print(shape.format(n_1=self.numerator_1, n_2=self.numerator_2,
                               action=self.action, d_1=self.denominator_1,
                               d_2=self.denominator_2))

        elif self.result_numerator == 1 and self.result_denominator == 1:
            shape = (
                """
                {n_1}      {n_2}      
                --  {action}  --  =   1
                {d_1}      {d_2}       
                """
            )
            print(shape.format(n_1=self.numerator_1, n_2=self.numerator_2,
                               action=self.action, d_1=self.denominator_1,
                               d_2=self.denominator_2))

        else:

            shape = (
                """
                {n_1}      {n_2}      {n_3}
                --  {action}  --  =  ---
                {d_1}      {d_2}      {d_3}
                """
            )

            print(shape.format(n_1=self.numerator_1, n_2=self.numerator_2,
                               action=self.action, d_1=self.denominator_1,
                               d_2=self.denominator_2,
                               n_3=self.result_numerator,
                               d_3=self.result_denominator))

    def order_of_commands(self):
        """
        the order of commands for the correct operation
        of the calculator
        """

        while True:
            self.information()
            if self.initialization() == 'off':
                break
            self.applying_actions()
            self.show_result()


my_calculator = Calculator()
my_calculator.order_of_commands()
