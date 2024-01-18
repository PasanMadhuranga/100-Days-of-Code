class MenuItem:
    def __init__(self, name: str, cost: float, ingredients: dict):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("espresso", 1.5, {"Water": 50, "Coffee": 18, }),
            MenuItem("latte", 2.5, {"Water": 200, "Milk": 150, "Coffee": 24, }),
            MenuItem("cappuccino", 3.0, {"Water": 250, "Milk": 100, "Coffee": 24, }),
        ]

    def get_items(self):
        """Returns all the names of the available menu items as a concatenated string."""
        name_of_items = ""
        for item in self.menu:
            name_of_items += item.name + "/"

        return name_of_items[:-1]

    def find_drink(self, order_name:str):
        """Searches the menu for a particular drink by name.
        Returns a MenuItem object if it exists, otherwise returns None."""
        for item in self.menu:
            if order_name == item.name:
                return item
        return None
