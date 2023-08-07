class MenuManager:
    def __init__(self, menu):
        """creates new instance of MenuManager with menu (list of dishies)"""
        self.menu = menu

    def add_item(self, name, price, spice, gluten):
        """append new dish to menu"""
        self.menu.append(
            {"name": name, "price": price, "spice": spice, "gluten": gluten}
        )

    def update_item(self, name, price, spice, gluten):
        """update dish if it is found in menu"""
        target = None
        for dish in self.menu:
            if dish["name"] == name:
                target = dish
                break

        if target is None:
            print("dish is not in the menu!")
            return

        target.update({"price": price, "spice": spice, "gluten": gluten})

    def remove_item(self, name):
        """remove dish if it exists in menu"""
        target = None
        for dish in self.menu:
            if dish["name"] == name:
                target = dish
                break

        if target is None:
            print("dish is not in the menu!")
            return

        self.menu.remove(target)
        print("updated menu:")
        self.print_menu()

    def print_menu(self):
        for dish in self.menu:
            print(dish)


# Example
menu_manager = MenuManager(
    [
        {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
        {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
        {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
        {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
        {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True},
    ]
)

menu_manager.add_item("Cheeseburger", 20, "A", False)

menu_manager.update_item("Soup", 14, "B", True)  # legal update
menu_manager.update_item("Soup with meet", 14, "B", True)  # illegal update

menu_manager.remove_item("Salad")  # legal remove operation
menu_manager.remove_item("Georgian Salad")  # illegal remove operation
