class CustomError(Exception):
    """this is a class with an error"""

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return (
            f'CustomError, {self.message}' if self.message else
            f'CustomError, default error'
        )


class CustomError1(CustomError):
    """this is a class with an error of the first type"""
    pass


class CustomError2(CustomError):
    """this is a class with an error of the second type"""
    pass
