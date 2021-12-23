# -*- coding: utf-8 -*-
# @CreateTime : 2021/12/23 13:51
# @Author     : 潘其威(PanEa)
# @File       : pizza_test_drive.py
# @Description:
# @LastEditBy :

import os

from models.pizza import ny_style_pizza, chicago_style_pizza
from models.stores import NYStylePizzaStore, ChicagoStylePizzaStore


class PizzaTestDrive:
    supported_pizza_store = {
        NYStylePizzaStore.name: NYStylePizzaStore(),
        ChicagoStylePizzaStore.name: ChicagoStylePizzaStore()
    }

    def run(self):
        id2store = {
            i: name for i, name in enumerate(self.supported_pizza_store.keys())
        }
        while True:
            try:
                store_ids_str = "\n".join(
                        [f"{i}: {name}" for i, name in id2store.items()]
                    )
                store_id = input(
                    "Please choose a pizza store:\n" +
                    store_ids_str +
                    "\nyour choice(<Ctrl+C> & <Enter> to exit simulation): "
                )
                if not store_id.isnumeric():
                    store_id = "-1"
                store_id = int(eval(store_id))
                if store_id in id2store:
                    store = self.supported_pizza_store[id2store[store_id]]
                    print(f"Hello! Welcome to the [{store.name}]!")

                    pizza_names = list(store.supported_pizza.keys())
                    while True:
                        pizza_id = input(
                            "Please choose the pizza you like:\n" +
                            "\n".join(
                                [f"{i}: {name}" for i, name in enumerate(pizza_names)]
                            ) +
                            "\nyour choice: "
                        )
                        if not pizza_id.isnumeric():
                            pizza_id = "-1"
                        pizza_id = int(eval(pizza_id))
                        if pizza_id not in list(range(len(pizza_names))):
                            print(
                                f"sorry, the pizza id [{pizza_id}] you choose is not exists, "
                                f"please choose one of {list(range(len(pizza_names)))}"
                            )
                        else:
                            break
                    pizza_name = pizza_names[pizza_id]
                    store.order_pizza(pizza_name)
                    print(f"[{pizza_name}] is prepared, please enjoy your pizza!")
                    os.system("cls")
                else:
                    print(
                        f"sorry, the store id [{store_id}] you choose is not exists, "
                        f"please choose one of {list(id2store.keys())}"
                    )
                    os.system("cls")
                    continue
            except KeyboardInterrupt:
                print("May you have a great day!")
                break


if __name__ == "__main__":
    test_drive = PizzaTestDrive()
    test_drive.run()
