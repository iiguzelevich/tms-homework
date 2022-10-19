def generator(b: int | float, q: int | float):
    """
    geometric progression generator
    q - common ratio
    b - member of the progression
    0 < q < 1 - decreasing progression
    q < 0 - alternating progression
    q = 0 - stationary progression
    q != 0
    b != 0
    """

    while q != 0 and b != 0:
        b = b * q
        yield b


b = float(input(
    'enter the first member of the progression: '
))

q = float(input(
    'enter the common ratio of the progression: '
))

len_result = int(input(
    'enter the number of progression members in the list: '
))

member = generator(b, q)
result = [b]

while len(result) < len_result:
    member_n = next(member)
    result.append(member_n)

print(result)
# Задание с регуляркой сделаю позже
