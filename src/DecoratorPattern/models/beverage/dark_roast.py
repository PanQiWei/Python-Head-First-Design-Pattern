# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 23:41
# @Author     : 潘其威(PanEa)
# @File       : dark_roast.py
# @Description:
# @LastEditBy :

from .beverage import Beverage


class DarkRoast(Beverage):
    """深烘焙咖啡"""

    _description = "Dark Roast Coffee"

    def cost(self):
        return 2.19
