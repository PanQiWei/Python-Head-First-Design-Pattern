# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 16:29
# @Author     : 潘其威(PanEa)
# @Company    : Gemsouls
# @File       : decoy_duck.py
# @Description:
# @LastEditBy :

from duck import Duck
from duck_behaviors import FlyNoWay, MuteQuack


class DecoyDuck(Duck):
    """诱饵鸭"""

    _fly_behavior = FlyNoWay()
    _quack_behavior = MuteQuack()

    def swim(self):
        print("Decoy duck swimming.")

    def display(self):
        print("I'm a decoy duck.")


if __name__ == "__main__":
    duck = DecoyDuck()
    print(duck.fly_behavior)
    print(duck.quack_behavior)
    duck.perform_fly()
    duck.perform_quack()
    duck.swim()
    duck.display()
