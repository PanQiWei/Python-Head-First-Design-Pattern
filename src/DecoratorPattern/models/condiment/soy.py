# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 23:48
# @Author     : 潘其威(PanEa)
# @File       : soy.py
# @Description:
# @LastEditBy :

from .condiment import Condiment
from ..beverage import Size


class Soy(Condiment):
    """豆奶"""

    _description = "Soy"

    @property
    def description(self):
        return self.beverage.description + f", {self._description}"

    def cost(self):
        cost = self.beverage.cost()
        if self.beverage.size == Size.TALL:
            cost += 0.2
        elif self.beverage.size == Size.GRANDE:
            cost += 0.35
        elif self.beverage.size == Size.VENTI:
            cost += 0.5
        return cost
