# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/23 12:55
# @Author     : 潘其威(PanEa)
# @File       : simple_pizza_factory.py
# @Description:
# @LastEditBy :


from pizza import *


class SimplePizzaFactory:
    def create_pizza(self, pizza_name: str):
        pizza = None

        if pizza_name == CalmPizza.name:
            pizza = CalmPizza()
        elif pizza_name == CheesePizza.name:
            pizza = CheesePizza()
        elif pizza_name == PepperoniPizza.name:
            pizza = PepperoniPizza()
        elif pizza_name == VeggiePizza.name:
            pizza = VeggiePizza()

        return pizza
