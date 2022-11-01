"""This module multiplies by zero
"""
from prettytable import PrettyTable


def just_mult(your_number: int) -> str:
    """
    Multiplies by zero.
    @param your_number: your number
    :return: a table with your number and result

    ```
    +-------------+--------------------------------------+
    | your number | the result of multiplication by zero |
    +-------------+--------------------------------------+
    |     1000    |                  0                   |
    +-------------+--------------------------------------+
    ```
    """

    result = your_number * 0

    table = PrettyTable(
        ['your number', 'the result of multiplication by zero']
    )
    table.add_row([your_number, result])

    return table.get_string()

