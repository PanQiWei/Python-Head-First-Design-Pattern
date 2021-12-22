# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 23:41
# @Author     : 潘其威(PanEa)
# @File       : decaf.py
# @Description:
# @LastEditBy :

from .beverage import Beverage


class Decaf(Beverage):
    """低因咖啡"""

    _description = "Decaf"

    def cost(self):
        return 2.99
