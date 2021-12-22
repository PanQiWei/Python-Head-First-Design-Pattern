# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 19:07
# @Author     : 潘其威(PanEa)
# @File       : statistics_display.py
# @Description:
# @LastEditBy :

import threading
import time

from ..interfaces import Observer, DisplayElement
from ..subjects import WeatherDataSubject


class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self, subject: WeatherDataSubject):
        self._subject = subject
        subject.register_observer(self)

        self._temperature_past10s = []
        self._humidity_past10s = []
        self._pressure_past10s = []

        threading.Thread(target=self.display, daemon=True).start()

    def update(self, temp: float, humidity: float, pressure: float):
        self._temperature_past10s.append(temp)
        self._humidity_past10s.append(humidity)
        self._pressure_past10s.append(pressure)

    def display(self):
        while True:
            if not self._temperature_past10s:
                _temperature_past10s = [0]
            else:
                _temperature_past10s = self._temperature_past10s
            if not self._humidity_past10s:
                _humidity_past10s = [0]
            else:
                _humidity_past10s = self._humidity_past10s
            if not self._pressure_past10s:
                _pressure_past10s = [0]
            else:
                _pressure_past10s = self._pressure_past10s
            print(
                f"[{self.__class__.__name__}]-->Statistics Past 10 seconds:\n"
                f"[{self.__class__.__name__}]-->Temperature: "
                f"(avg){sum(_temperature_past10s) / len(_temperature_past10s): .2f}F\t"
                f"(max){max(_temperature_past10s)}F\t"
                f"(min){min(_temperature_past10s)}F\n"
                f"[{self.__class__.__name__}]-->Humidity: "
                f"(avg){sum(_humidity_past10s) / len(_humidity_past10s): .2f}%\t"
                f"(max){max(_humidity_past10s)}%\t"
                f"(min){min(_humidity_past10s)}%\n"
                f"[{self.__class__.__name__}]-->Pressure: "
                f"(avg){sum(_pressure_past10s) / len(_pressure_past10s): .2f}Pa\t"
                f"(max){max(_pressure_past10s)}Pa\t"
                f"(min){min(_pressure_past10s)}Pa\n"
            )
            self._refresh()
            time.sleep(10)

    def _refresh(self):
        self._temperature_past10s = []
        self._humidity_past10s = []
        self._pressure_past10s = []
