from random import randint
import math
import matplotlib.pyplot as plt


class MyNum:
    min_num = 0

    @classmethod
    def check(cls, arg):
        return cls.min_num <= arg

    def __init__(self, *args):
        self.list_args = []
        self.args = args
        for i in self.args[0]:
            if MyNum.check(i):
                self.list_args.append(i)

    def func_sum(self):
        return math.fsum(self.list_args)

    @staticmethod
    def func_factorial(your_num: int) -> int:
        f = 1
        for i in range(1, your_num + 1):
            f *= i
        return f

    def get_list_arg_sort(self):
        self.list_args.sort()
        return self.list_args

    def get_list_arg(self):
        return self.list_args

    def get_list_x(self):
        list_x = []
        for i in self.list_args:
            if i not in list_x:
                list_x.append(i)
                list_x.sort()
        return list_x

    def get_list_y(self):
        list_y = [self.get_list_arg_sort().count(i) for i in self.get_list_x()]
        return list_y


list_num = [randint(-1, 10) for i in range(2000)]

num = MyNum(list_num)

print(list(set(list_num)))
print(num.get_list_x())

print(num.func_sum())
print(num.func_factorial(randint(1, 10)))

axis_x = num.get_list_x()
axis_y = num.get_list_y()
plt.figure(figsize=(9, 5))
plt.subplot(132)
plt.bar(axis_x, axis_y)
plt.plot(axis_x, axis_y)
plt.show()
