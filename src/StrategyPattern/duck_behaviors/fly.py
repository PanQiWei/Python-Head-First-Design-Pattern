# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 15:51
# @Author     : 潘其威(PanEa)
# @File       : fly.py
# @Description:
# @LastEditBy :


from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    _description: str

    @abstractmethod
    def fly(self):
        pass

    def __repr__(self):
        return self._description

    def __str__(self):
        return self.__repr__()


class FlyWithWings(FlyBehavior):
    _description = "flying with wings."

    def fly(self):
        return "I'm flying!"


class FlyNoWay(FlyBehavior):
    _description = "can not fly."

    def fly(self):
        return "I can't fly!"
