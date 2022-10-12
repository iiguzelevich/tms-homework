from dataclasses import dataclass


@dataclass()
class Flowers:

    type_flower: str
    quality: str
    price: int
    color: str
    quantity: int


class Bouquet:

    def __init__(self, _flowers):
        self.flowers = _flowers

    def calculation_of_the_discount(self):

        if self.flowers.quality == 'high':
            return 1

        elif self.flowers.quality == 'medium':
            return 0.75

        elif self.flowers.quality == 'so so':
            return 0.55

    def cost_of_the_bouquet(self):
        cost = (
                self.calculation_of_the_discount()
                * self.flowers.quantity
                * self.flowers.price
        )
        return cost

    def __more_information(self):
        return f'https://en.wikipedia.org/wiki/{self.flowers.type_flower}'

    def __str__(self):
        return (
            f'The price of this bouquet: {self.cost_of_the_bouquet()}\n'
            f'{self.show_information_about_your_bouquet()}'
            f'If you want to see more information about this flower:'
            f' {self.__more_information()}\n'
        )

    def show_information_about_your_bouquet(self):
        return (
            f'Your bouquet consists of {self.flowers.quantity} '
            f'- {self.flowers.color} '
            f'{self.flowers.type_flower}\n'
        )


flower_rose = Flowers(
    type_flower='rose',
    quality='medium',
    price=100,
    color='scarlet',
    quantity=1000000,
)

flower_tulip = Flowers(
    type_flower='tulip',
    quality='high',
    price=70,
    color='yellow',
    quantity=23,
)

flower_cornflower = Flowers(
    type_flower='cornflower',
    quality='medium',
    price=25,
    color='blue',
    quantity=100,
)

bouquet_1 = Bouquet(flower_rose)
bouquet_2 = Bouquet(flower_tulip)
bouquet_3 = Bouquet(flower_cornflower)

print(bouquet_1)
print(bouquet_2)
print(bouquet_3)
