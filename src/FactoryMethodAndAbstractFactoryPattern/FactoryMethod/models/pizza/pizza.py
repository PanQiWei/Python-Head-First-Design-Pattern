# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/23 12:56
# @Author     : 潘其威(PanEa)
# @File       : pizza.py
# @Description:
# @LastEditBy :

import random
import time
from typing import List


class Pizza:
    name: str = "Unknown Pizza"
    dough: str = "Unknown Dough"
    sauce: str = "Unknown Sauce"
    toppings: List[str] = []

    def prepare(self):
        print(f"Preparing [{self.name}]")
        print(f"Tossing dough...")
        time.sleep(random.uniform(0.5, 1))
        print(f"Adding sauce...")
        time.sleep(random.uniform(0.5, 1))
        print(f"Adding toppings:")
        for topping in self.toppings:
            print(f"\t{topping}")
            time.sleep(random.uniform(0.5, 1))
        if not self.toppings:
            print(f"\t(no topping is added.)")

    def bake(self):
        print(f"Bake for 25 minutes at 350.")
        time.sleep(random.uniform(1, 2))

    def cut(self):
        print(f"Cutting the pizza into diagonal slices")
        time.sleep(random.uniform(0.5, 1))

    def box(self):
        print(f"Place pizza in official PizzaStore box")
        time.sleep(random.uniform(0.5, 1))


class CheesePizza(Pizza):
    name: str = "Cheese Pizza"


class PepperoniPizza(Pizza):
    name: str = "Pepperoni Pizza"


class ClamPizza(Pizza):
    name: str = "Clam Pizza"


class VeggiePizza(Pizza):
    name: str = "Veggie Pizza"
