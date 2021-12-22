# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 23:28
# @Author     : 潘其威(PanEa)
# @File       : starbuzz.py
# @Description:
# @LastEditBy :

from typing import List

from models.beverage import *
from models.condiment import *


class StarbuzzCoffee:
    supported_beverages = [
        Espresso, DarkRoast, Decaf, HouseBlend
    ]
    supported_condiments = [
        Mocha, Soy, Whip
    ]

    def make_coffee(self, size: Size, beverage: Beverage, condiments: List[Condiment]):
        coffee = self._make_coffee(size, condiments + [beverage])
        print(f"[{coffee.description}] costs: {coffee.cost(): .2f}$")

    def _make_coffee(self, size: Size, components: List[Beverage]):
        component = components[0]
        other_components = components[1:]
        if not other_components:
            return component(size)
        else:
            return component(self._make_coffee(size, other_components))


if __name__ == "__main__":
    import random
    candidate_beverages = StarbuzzCoffee.supported_beverages
    candidate_condiments = StarbuzzCoffee.supported_condiments

    starbuzz = StarbuzzCoffee()
    for _ in range(10):
        beverage = random.choice(candidate_beverages)
        condiments = random.sample(candidate_condiments, k=random.randrange(1, len(candidate_condiments)))
        size = getattr(Size, random.choice(list(Size.__members__.keys())))
        starbuzz.make_coffee(size, beverage, condiments)
