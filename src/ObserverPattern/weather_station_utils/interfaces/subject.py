# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 17:31
# @Author     : 潘其威(PanEa)
# @File       : subject.py
# @Description:
# @LastEditBy :

from abc import ABC, abstractmethod

from .observer import Observer


class Subject(ABC):
    @abstractmethod
    def register_observer(self, o: Observer):
        pass

    @abstractmethod
    def remove_observer(self, o: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass
