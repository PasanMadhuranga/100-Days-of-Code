print("Welcome to the tip calculator.")

total = float(input("What was the total bill? $"))
num_of_people = int(input("How many people to split the bill? "))
tip_percentage = float(input("What percentage tip would you like to give? "))

one_should_pay = round((total * (1 + (tip_percentage / 100))) / num_of_people, 2)

print(f"Each person should pay: ${one_should_pay}")
