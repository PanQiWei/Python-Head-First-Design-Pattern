# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 23:31
# @Author     : 潘其威(PanEa)
# @File       : beverage.py
# @Description: 定义所有饮料的基类
# @LastEditBy :

from abc import ABC, abstractmethod
from enum import Enum


class Size(Enum):
    TALL = "tall"  # 小杯
    GRANDE = "grande"  # 中杯
    VENTI = "venti"  # 大杯


class Beverage(ABC):
    _description: str = "Unknown Beverage"

    def __init__(self, size: Size):
        self._size = size

    @property
    def description(self):
        return self._description + f"({self._size.value})"

    @abstractmethod
    def cost(self):
        pass

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size: Size):
        self._size = size
