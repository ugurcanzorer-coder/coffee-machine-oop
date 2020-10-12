# Write your code here
# Write your code here
"""print(
Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!
"""
"""
water_has = int(input("Write how many ml of water the coffee machine has: "))
milk_has = int(input("Write how many ml of milk the coffee machine has: "))
beans_has = int(input("Write how many grams of coffee beans the coffee machine has"))
cups_of_coffee = int(input("Write how many cups of coffee you will need:"))
print("For {} cups of coffee you will need:".format(cups_of_coffee))
needed_water = 200 * cups_of_coffee
needed_milk = 50 * cups_of_coffee
needed_beans = 15 * cups_of_coffee
print("{} ml of water".format(needed_water))
print("{} ml of milk".format(needed_milk))
print("{} g of coffee beans".format(needed_beans))

if water_has >= needed_water and milk_has >= needed_milk and beans_has >= needed_beans:
    if int(water_has / needed_water) == 1 or int(milk_has / needed_milk) == 1 or int(beans_has / needed_beans) == 1:
        print("Yes, I can make that amount of coffee")
    else:
        minimum = min(int(water_has / needed_water), int(milk_has / needed_milk), int(beans_has / needed_beans)) - 1
        print("Yes, I can make that amount of coffee (and even {} more than that)".format(minimum))
else:
    minimum = int(min(water_has / 200, milk_has / 50, beans_has / 15))
    print("No, I can make only {} cups of coffee".format(minimum))
"""

import sys


class CoffeeMachine:
    def __init__(self, water_has, milk_has, beans_has, cups_has, money_has):
        self.water_has = water_has
        self.milk_has = milk_has
        self.beans_has = beans_has
        self.cups_has = cups_has
        self.money_has = money_has

    def __str__(self):

        return """
The coffee machine has: 
{} of water
{} of milk 
{} of coffee beans
{} of disposable cups
{} of money
        """.format(self.water_has, self.milk_has, self.beans_has, self.cups_has, self.money_has)

    def choose(self):
        coffee_choice = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n")
        if coffee_choice == "back":
            pass
        else:
            try:
                coffee_choice = int(coffee_choice)
                self.buy(coffee_choice)
            except ValueError:
                print("ValueError")
                return

    def buy(self, coffee_choice):
        i = coffee_choice - 1
        kahveler = [espresso, latte, cappuccino]
        condition1 = kahveler[i].water <= self.water_has
        condition2 = kahveler[i].milk <= self.milk_has
        condition3 = kahveler[i].beans <= self.beans_has
        condition4 = 0 < self.cups_has
        conditions = [condition1, condition2, condition3, condition4]
        if condition1 and condition2 and condition3 and condition4:
            print("I have enough resources, making you a coffee!\n")
            self.water_has -= kahveler[i].water
            self.milk_has -= kahveler[i].milk
            self.beans_has -= kahveler[i].beans
            self.money_has += kahveler[i].cost
            self.cups_has -= 1
        else:
            for i in range(len(conditions)):
                if not conditions[i]:
                    if i == 0:
                        keyword = "water"
                    elif i == 1:
                        keyword = "milk"
                    elif i == 2:
                        keyword = "coffee beans"
                    else:
                        keyword = "disposable cups"
                    print("Sorry, not enough {}!\n".format(keyword))

    def fill(self):
        add_water = int(input("Write how many ml of water do you want to add: \n"))
        add_milk = int(input("Write how many ml of milk do you want to add: \n"))
        add_beans = int(input("Write how many  grams of coffee beans do you want to add: \n"))
        add_cups = int(input("Write how many disposable cups of coffee do you want to add: \n\n"))

        self.water_has += add_water
        self.milk_has += add_milk
        self.beans_has += add_beans
        self.cups_has += add_cups

        return

    def take(self):
        print("\nI gave you ${}\n".format(self.money_has))
        self.money_has = 0
        return

    def empty(self):
        self.water_has = 0
        self.cups_has = 0
        self.beans_has = 0
        self.milk_has = 0
        self.money_has = 0

    def __len__(self):
        return self.cups_has


class Kahveler:
    def __init__(self, water, milk, beans, cost):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cost = cost


espresso = Kahveler(250, 0, 16, 4)
latte = Kahveler(350, 75, 20, 7)
cappuccino = Kahveler(200, 100, 12, 6)
coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    input_value = input("Write action (buy, fill, take, remaining, empty, cups, exit)\n")
    if input_value == "buy":
        coffee_machine.choose()
    elif input_value == "fill":
        coffee_machine.fill()
    elif input_value == "take":
        coffee_machine.take()
    elif input_value == "remaining":
        print(coffee_machine)
    elif input_value == "cups":
        print("Remaining cups: {len(coffee_machine)}")
    elif input_value == "exit":
        sys.exit()
    elif input_value == "empty":
        coffee_machine.empty()



