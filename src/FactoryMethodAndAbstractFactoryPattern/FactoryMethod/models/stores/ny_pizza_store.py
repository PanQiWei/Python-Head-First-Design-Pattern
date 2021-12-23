# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/23 13:26
# @Author     : 潘其威(PanEa)
# @File       : ny_pizza_store.py
# @Description:
# @LastEditBy :

from .basic_pizza_store import PizzaStore
from ..pizza import ny_style_pizza


class NYStylePizzaStore(PizzaStore):
    name = "NY Style Pizza Store"
    supported_pizza = {
        ny_style_pizza.NYStyleClamPizza.name: ny_style_pizza.NYStyleClamPizza,
        ny_style_pizza.NYStylePepperoniPizza.name: ny_style_pizza.NYStylePepperoniPizza,
        ny_style_pizza.NYStyleCheesePizza.name: ny_style_pizza.NYStyleCheesePizza,
        ny_style_pizza.NYStyleVeggiePizza.name: ny_style_pizza.NYStyleVeggiePizza
    }

    def create_pizza(self, pizza_name: str):
        if pizza_name in self.supported_pizza:
            return self.supported_pizza[pizza_name]()
        return None
