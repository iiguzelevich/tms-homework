class MyMetaClass(type):

    def add_attrs(cls):
        return (
            f'Metaclasses are deeper magic than 99% of users should \n'
            f'ever worry about. If you wonder whether you need them, \n'
            f'you don’t '
            f'(the people who actually need them know with certainty \n'
            f'that they need them, and don’t need an explanation about why).\n'
            f'— Tim Peters\n'
        )

    def __init__(cls, name, base, attrs):
        attrs.update({'method_1': cls.add_attrs})
        super().__init__(name, base, attrs)
        cls.zero = 0
        cls.one = 1
        cls.add_attrs()


class MySomeClass(metaclass=MyMetaClass):
    pass


my_some_object = MySomeClass

print(my_some_object.one)
print(my_some_object.zero)
print(my_some_object.add_attrs())
