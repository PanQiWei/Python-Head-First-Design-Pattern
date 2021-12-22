# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/22 16:32
# @Author     : 潘其威(PanEa)
# @File       : model_duck.py
# @Description:
# @LastEditBy :

from duck import Duck
from duck_behaviors import FlyBehavior, QuackBehavior
from duck_behaviors import FlyNoWay, Quack


class ModelDuck(Duck):
    """模型鸭"""
    _fly_behavior = FlyNoWay()
    _quack_behavior = Quack()

    def swim(self):
        print("Model duck swimming.")

    def display(self):
        print("I'm a model duck.")


class FlyRocketPowered(FlyBehavior):
    _description = "flying with a rocket."

    def fly(self):
        return "I'm flying with a rocket!"


if __name__ == "__main__":
    duck = ModelDuck()

    duck.perform_quack()
    duck.perform_fly()
    duck.fly_behavior = FlyRocketPowered()
    duck.perform_fly()
