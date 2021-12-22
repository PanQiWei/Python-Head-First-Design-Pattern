# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 23:37
# @Author     : 潘其威(PanEa)
# @File       : espresso.py
# @Description:
# @LastEditBy :

from .beverage import Beverage


class Espresso(Beverage):
    """意式浓缩咖啡"""

    _description = "Espresso"

    def cost(self):
        return 1.99
