# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 15:46
# @Author     : 潘其威(PanEa)
# @File       : duck.py
# @Description:
# @LastEditBy :


from abc import ABC, abstractmethod
from duck_behaviors import FlyBehavior, QuackBehavior


class Duck(ABC):
    """鸭子超类"""

    _fly_behavior: FlyBehavior
    _quack_behavior: QuackBehavior

    def perform_fly(self):
        print(self._fly_behavior.fly())

    def perform_quack(self):
        print(self._quack_behavior.quack())

    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def display(self):
        pass

    @property
    def fly_behavior(self):
        return str(self._fly_behavior)

    @fly_behavior.setter
    def fly_behavior(self, fly_behavior: FlyBehavior):
        self._fly_behavior = fly_behavior

    @property
    def quack_behavior(self):
        return str(self._quack_behavior)

    @quack_behavior.setter
    def quack_behavior(self, quack_behavior: QuackBehavior):
        self._quack_behavior = quack_behavior
