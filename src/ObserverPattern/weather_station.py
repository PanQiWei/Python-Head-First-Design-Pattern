# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 19:24
# @Author     : 潘其威(PanEa)
# @File       : weather_station.py
# @Description:
# @LastEditBy :

import random
import time

from weather_station_utils.subjects import WeatherDataSubject
from weather_station_utils.displays import CurrentConditionsDisplay, StatisticsDisplay


class WeatherStation:
    def __init__(self):
        self.subject = WeatherDataSubject()
        self.current_conditions_display = CurrentConditionsDisplay(self.subject)
        self.statistics_display = StatisticsDisplay(self.subject)

    def run(self):
        for _ in range(100):
            temp = random.randrange(76, 84)
            humidity = random.randrange(65, 90)
            pressure = random.randrange(28, 32)
            self.subject.set_measurements(temp, humidity, pressure)
            time.sleep(0.5)


if __name__ == "__main__":
    station = WeatherStation()
    station.run()
