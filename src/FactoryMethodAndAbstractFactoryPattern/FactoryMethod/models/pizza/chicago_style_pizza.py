# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/23 13:25
# @Author     : 潘其威(PanEa)
# @File       : chicago_style_pizza.py
# @Description:
# @LastEditBy :

import random
import time

from .pizza import *


class ChicagoStyleCheesePizza(CheesePizza):
    name = "Chicago Style " + CheesePizza.name
    dough = "Extra Thick Crust Dough"
    sauce = "Plum Tomato Sauce"
    toppings = ["Shredded Mozzarella Cheese"]

    def cut(self):
        print("Cutting the pizza into square slices")
        time.sleep(random.uniform(0.5, 1))


class ChicagoStylePepperoniPizza(PepperoniPizza):
    name = "Chicago Style " + PepperoniPizza.name


class ChicagoStyleClamPizza(ClamPizza):
    name = "Chicago Style " + ClamPizza.name


class ChicagoStyleVeggiePizza(VeggiePizza):
    name = "Chicago Style " + VeggiePizza.name
