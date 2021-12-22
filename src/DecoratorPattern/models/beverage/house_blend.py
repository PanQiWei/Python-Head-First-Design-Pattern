# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 23:39
# @Author     : 潘其威(PanEa)
# @File       : house_blend.py
# @Description:
# @LastEditBy :

from .beverage import Beverage


class HouseBlend(Beverage):
    """家常咖啡"""

    _description = "House Blend Coffee"

    def cost(self):
        return 0.89
