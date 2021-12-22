# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 17:36
# @Author     : 潘其威(PanEa)
# @Company    : Gemsouls
# @File       : observer.py
# @Description:
# @LastEditBy :


from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float):
        pass
