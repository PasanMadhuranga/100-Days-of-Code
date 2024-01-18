from menu import MenuItem


class CoffeeMaker:
    def __init__(self):
        with open("resources.txt") as file:
            resources_list = file.readlines()
            resources_list = [line.rstrip() for line in resources_list]
        self.resources = {}
        for ingredient in resources_list:
            ingredient_list = ingredient.split(",")
            self.resources[ingredient_list[0]] = float(ingredient_list[1])



    def report(self):
        """Returns a report of all resources."""
        resources_report = f"Water: {self.resources['Water']} ml\nMilk: {self.resources['Milk']} ml\n" \
                           f"Coffee: {self.resources['Coffee']} g "

        return resources_report

    def is_resource_sufficient(self, drink: MenuItem):
        """Returns True when the drink order can be made, False if ingredients are insufficient."""
        for (ingredient, quantity) in drink.ingredients.items():
            if self.resources[ingredient] < quantity:
                return False
        return True

    def make_coffee(self, drink: MenuItem):
        """Deducts the required ingredients from the resources."""
        with open("resources.txt", mode="w") as file:
            for (ingredient, quantity) in drink.ingredients.items():
                self.resources[ingredient] = self.resources[ingredient] - quantity
                file.write(f"{ingredient},{self.resources[ingredient]}\n")
