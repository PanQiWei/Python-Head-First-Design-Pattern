# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 16:28
# @Author     : 潘其威(PanEa)
# @File       : rubber_duck.py
# @Description:
# @LastEditBy :

from duck import Duck
from duck_behaviors import FlyNoWay, Squeak


class RubberDuck(Duck):
    """橡皮鸭"""

    _fly_behavior = FlyNoWay()
    _quack_behavior = Squeak()

    def swim(self):
        print("Rubber duck swimming.")

    def display(self):
        print("I'm a rubber duck.")


if __name__ == "__main__":
    duck = RubberDuck()
    print(duck.fly_behavior)
    print(duck.quack_behavior)
    duck.perform_fly()
    duck.perform_quack()
    duck.swim()
    duck.display()
