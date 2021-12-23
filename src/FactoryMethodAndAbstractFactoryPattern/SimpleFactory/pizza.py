# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/23 12:56
# @Author     : 潘其威(PanEa)
# @File       : pizza.py
# @Description:
# @LastEditBy :


class Pizza:
    name: str = "Unknown Pizza"

    def prepare(self):
        print(f"Preparing [{self.name}]")

    def bake(self):
        print(f"Baking [{self.name}]")

    def cut(self):
        print(f"Cutting [{self.name}]")

    def box(self):
        print(f"Boxing [{self.name}]")


class CheesePizza(Pizza):
    name: str = "Cheese Pizza"


class PepperoniPizza(Pizza):
    name: str = "Pepperoni Pizza"


class CalmPizza(Pizza):
    name: str = "Calm Pizza"


class VeggiePizza(Pizza):
    name: str = "Veggie Pizza"
