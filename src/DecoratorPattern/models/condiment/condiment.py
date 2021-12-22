# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 23:33
# @Author     : 潘其威(PanEa)
# @File       : condiment.py
# @Description: 定义调料的基类
# @LastEditBy :

from abc import ABC, abstractmethod

from ..beverage import Beverage, Size


class Condiment(Beverage):
    """
    调料是装饰者类，因此需要继承自饮料类
    """
    _description = "Unknown condiment"

    def __init__(self, beverage: Beverage):
        self.beverage = beverage
        super(Condiment, self).__init__(beverage.size)

    @abstractmethod
    def cost(self):
        pass

    @property
    @abstractmethod
    def description(self):
        pass

    @property
    def size(self):
        return self.beverage.size
