# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 23:45
# @Author     : 潘其威(PanEa)
# @File       : mocha.py
# @Description:
# @LastEditBy :

from .condiment import Condiment
from ..beverage import Size


class Mocha(Condiment):
    """摩卡"""
    _description = "Mocha"

    @property
    def description(self):
        return self.beverage.description + f", {self._description}"

    def cost(self):
        cost = self.beverage.cost()
        if self.beverage.size == Size.TALL:
            cost += 0.2
        elif self.beverage.size == Size.GRANDE:
            cost += 0.3
        elif self.beverage.size == Size.VENTI:
            cost += 0.4
        return cost
