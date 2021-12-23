# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/23 13:02
# @Author     : 潘其威(PanEa)
# @File       : pizza_store.py
# @Description:
# @LastEditBy :

from pizza import *
from simple_pizza_factory import SimplePizzaFactory


class PizzaStore:
    supported_pizza = [CheesePizza.name, CalmPizza.name, PepperoniPizza.name, VeggiePizza.name]

    def __init__(self):
        self._factory = SimplePizzaFactory()

    def order_pizza(self, pizza_name: str):
        pizza = self._factory.create_pizza(pizza_name)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        print(f"[{pizza.name}] finished.")

        return pizza


if __name__ == "__main__":
    import random

    pizza_store = PizzaStore()
    for _ in range(10):
        pizza_name = random.choice(pizza_store.supported_pizza)
        print(pizza_name)
        pizza_store.order_pizza(pizza_name)
        print("-" * 44)
