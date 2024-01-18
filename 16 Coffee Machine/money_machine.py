class MoneyMachine:
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        with open("profit.txt") as file:
            self.profit = float(file.read().strip())

    def report(self):
        """Prints the current profit"""
        return f"Money: ${self.profit}"

    def make_payment(self, cost: float):
        """Returns True when payment is accepted, or False if insufficient."""

        def process_coins():
            """Get the number of coins that user inserts to the machine."""
            cash_received = 0
            print("Please insert coins.")
            for (coin_name, value) in self.COIN_VALUES.items():
                num_of_coins = int(input(f"How many {coin_name}?\n"))
                cash_received += num_of_coins * value
            return cash_received

        received_money = process_coins()
        if cost < received_money:
            self.profit += cost
            with open("profit.txt", mode="w") as file:
                file.write(str(self.profit))
            return f"Here is your change: ${round(received_money - cost, 2)}"
        return None
