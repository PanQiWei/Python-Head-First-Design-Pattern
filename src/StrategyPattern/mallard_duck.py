# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 16:22
# @Author     : 潘其威(PanEa)
# @File       : mallard_duck.py
# @Description:
# @LastEditBy :

from duck import Duck
from duck_behaviors import FlyWithWings, Quack


class MallardDuck(Duck):
    """绿头鸭"""

    _fly_behavior = FlyWithWings()
    _quack_behavior = Quack()

    def swim(self):
        print("Mallard duck swimming.")

    def display(self):
        print("I'm a mallard duck!")


if __name__ == "__main__":
    duck = MallardDuck()
    print(duck.fly_behavior)
    print(duck.quack_behavior)
    duck.perform_fly()
    duck.perform_quack()
    duck.swim()
    duck.display()
