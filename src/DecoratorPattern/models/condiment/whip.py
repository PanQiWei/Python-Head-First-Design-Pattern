# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 23:50
# @Author     : 潘其威(PanEa)
# @File       : whip.py
# @Description:
# @LastEditBy :

from .condiment import Condiment
from ..beverage import Size


class Whip(Condiment):
    """鲜奶油"""

    _description = "Whip"

    @property
    def description(self):
        return self.beverage.description + f", {self._description}"

    def cost(self):
        cost = self.beverage.cost()
        if self.beverage.size == Size.TALL:
            cost += 0.35
        elif self.beverage.size == Size.GRANDE:
            cost += 0.4
        elif self.beverage.size == Size.VENTI:
            cost += 0.45
        return cost
