# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 18:57
# @Author     : 潘其威(PanEa)
# @File       : current_condition_display.py
# @Description:
# @LastEditBy :

from ..interfaces import Observer, DisplayElement
from ..subjects import WeatherDataSubject


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, subject: WeatherDataSubject):
        self._subject = subject
        subject.register_observer(self)

        self._temperature = subject.temperature
        self._humidity = subject.humidity
        self._pressure = subject.pressure

    def update(self, temp: float, humidity: float, pressure: float):
        self._temperature = temp
        self._humidity = humidity
        self._pressure = pressure
        self.display()

    def display(self):
        print(
            f"[{self.__class__.__name__}]-->Current conditions: "
            f"{self._temperature:.2f} F degrees and "
            f"{self._humidity: .2f} % humidity"
        )
