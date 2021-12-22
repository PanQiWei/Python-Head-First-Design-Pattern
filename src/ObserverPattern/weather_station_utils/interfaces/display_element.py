# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 17:37
# @Author     : 潘其威(PanEa)
# @Company    : Gemsouls
# @File       : display_element.py
# @Description:
# @LastEditBy :

from abc import ABC, abstractmethod


class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass
