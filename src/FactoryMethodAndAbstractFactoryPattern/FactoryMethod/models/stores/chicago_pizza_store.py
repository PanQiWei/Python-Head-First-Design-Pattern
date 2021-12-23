# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/23 13:35
# @Author     : 潘其威(PanEa)
# @File       : chicago_pizza_store.py
# @Description:
# @LastEditBy :

from .basic_pizza_store import PizzaStore
from ..pizza import chicago_style_pizza


class ChicagoStylePizzaStore(PizzaStore):
    name = "Chicago Style Pizza Store"
    supported_pizza = {
        chicago_style_pizza.ChicagoStyleClamPizza.name : chicago_style_pizza.ChicagoStyleClamPizza,
        chicago_style_pizza.ChicagoStylePepperoniPizza.name: chicago_style_pizza.ChicagoStylePepperoniPizza,
        chicago_style_pizza.ChicagoStyleCheesePizza.name: chicago_style_pizza.ChicagoStyleCheesePizza,
        chicago_style_pizza.ChicagoStyleVeggiePizza.name: chicago_style_pizza.ChicagoStyleVeggiePizza
    }

    def create_pizza(self, pizza_name: str):
        if pizza_name in self.supported_pizza:
            return self.supported_pizza[pizza_name]()
        return None
