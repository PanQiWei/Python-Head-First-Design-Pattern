# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 17:42
# @Author     : 潘其威(PanEa)
# @Company    : Gemsouls
# @File       : weather_data.py
# @Description:
# @LastEditBy :

from typing import *

from ..interfaces import Subject, Observer


class WeatherDataSubject(Subject):
    # 因为在这里所有的观察者都会订阅同一个主题（即主题是唯一的），因此可以大胆地将之设置为类全局变量
    _observers: List[Observer] = list()
    _temperature: float = 0.0
    _humidity: float = 0.0
    _pressure: float = 0.0

    def register_observer(self, o: Observer):
        self._observers.append(o)

    def remove_observer(self, o: Observer):
        if o in self._observers:
            self._observers.remove(o)

    def notify_observers(self):
        for o in self._observers:
            o.update(self._temperature, self._humidity, self._pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure

        self.measurements_changed()

    @property
    def temperature(self):
        return self._temperature

    @property
    def humidity(self):
        return self._humidity

    @property
    def pressure(self):
        return self._pressure
