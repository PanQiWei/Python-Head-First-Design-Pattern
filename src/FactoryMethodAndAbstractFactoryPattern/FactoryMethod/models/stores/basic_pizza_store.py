# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/23 13:19
# @Author     : 潘其威(PanEa)
# @File       : basic_pizza_store.py
# @Description:
# @LastEditBy :

from abc import ABC, abstractmethod
from typing import List

from ..pizza import Pizza


class PizzaStore(ABC):
    name: str
    supported_pizza: List[Pizza]

    def order_pizza(self, pizza_name: str):
        pizza: Pizza = self.create_pizza(pizza_name)
        if not pizza:
            print(f"Sorry, [{pizza_name}] is not supported by [{self.__class__.__name__}]")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self, pizza_name: str):
        pass
