# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 15:51
# @Author     : 潘其威(PanEa)
# @File       : quack.py
# @Description:
# @LastEditBy :


from abc import ABC, abstractmethod


class QuackBehavior(ABC):
    _description: str

    @abstractmethod
    def quack(self):
        pass

    def __repr__(self):
        return self._description

    def __str__(self):
        return self.__repr__()


class Quack(QuackBehavior):
    _description = "making sound like 'quack'."

    def quack(self):
        return "Quack, quack, quack."


class Squeak(QuackBehavior):
    _description = "making sound like 'squeak'."

    def quack(self):
        return "Squeak, squeak, squeak"


class MuteQuack(QuackBehavior):
    _description = "can not make sound."

    def quack(self):
        return "...(can't make sound)"
