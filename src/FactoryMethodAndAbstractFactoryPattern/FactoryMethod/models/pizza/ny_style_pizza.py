# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/23 13:23
# @Author     : 潘其威(PanEa)
# @File       : ny_style_pizza.py
# @Description:
# @LastEditBy :

from .pizza import *


class NYStyleCheesePizza(CheesePizza):
    name = "NY Style " + CheesePizza.name
    dough = "Thin Crust Dough"
    sauce = "Marinara Sauce"
    toppings = ["Grated Reggiano Cheese"]


class NYStylePepperoniPizza(PepperoniPizza):
    name = "NY Style " + PepperoniPizza.name


class NYStyleClamPizza(ClamPizza):
    name = "NY Style " + ClamPizza.name


class NYStyleVeggiePizza(VeggiePizza):
    name = "NY Style " + VeggiePizza.name
