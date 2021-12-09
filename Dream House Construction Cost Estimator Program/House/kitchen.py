"""
This module contains the class Kitchen. To help this module run, room and feature modules are imported here.
"""

# Modules to import.

from House.room import Room
from House.feature import Feature

# List of possible kitchen attributes to choose from.

default_counter = Feature('blank', 0, 'counter')
counter1 = Feature('Granite', 3000, 'counter')  # Citation: (Thompson, 2021)
counter2 = Feature('Quartz', 4000, 'counter')  # Citation: (Thompson, 2021)
counter3 = Feature('Plastic laminate', 1000, 'counter')  # Citation: (HomeAdvisor, "...counter...")
counters = [counter1, counter2, counter3]

default_fridge = Feature('blank', 0, 'unit')
fridge1 = Feature('Stainless steel double door fridge', 3000, 'unit')  # Citation: (The Home Depot)
fridge2 = Feature('Stainless steel single door fridge', 1000, 'unit')   # Citation: (Lowe's, "...17.2...")
fridge3 = Feature('Non-stainless steel single door fridge', 500, 'unit')  # Citation: (Lowe's, "...18...")
fridges = [fridge1, fridge2, fridge3]

default_ksink = Feature('blank', 0, 'unit')
ksink1 = Feature('Single sink', 200, 'unit')  # Citation: (Lowe's, "...stainless steel single...")
ksink2 = Feature('Double sink', 250, 'unit')  # Citation: (Lowe's, "...stainless steel double...")
kitchen_sinks = [ksink1, ksink2]

class Kitchen(Room):
    """
    This class is a subclass of Room. It holds the Kitchen object and also prompts user to choose kitchen attributes.
    """

    def __init__(self, counter = default_counter, fridge = default_fridge, sink = default_ksink):
        """
        This is the initializer function for Kitchen.
        :param counter: The input should be of type Feature, and refers to the chosen counter top.
        :param fridge: The input should be of type Feature, and refers to the chosen fridge.
        :param sink: The input should be of type Feature, and refers to the chosen sink.
        """
        super().__init__()
        self.kcounter = counter
        self.fridge = fridge
        self.sink = sink
        self.type = 'kitchen'

    def set_kcounter(self):
        """
        This function sets the kitchen counter attribute after prompting user for input from set menu.
        """
        print("")
        while True:
            index = 1
            print("What kind of material do you want your kitchen countertop to be made of?")
            for counter in counters:  # Creating menu of counter tops to choose from.
                print(index, "-", counter)
                index += 1
            choice = input('Enter the corresponding number of your choice from the menu above: ')
            try:
                choice = int(choice)
            except:
                print("This is not a valid entry! Enter a number.\n")
                continue
            if choice == 1 or choice == 2 or choice == 3:
                break
            else:
                print("This is not a valid entry! Number must match a menu item.\n")
        self.attributes['kcounter'] = counters[choice - 1]
        self.kcounter = counters[choice - 1]
        self.kcounter.count = 1

    def get_kcounter(self):
        """
        This function returns the chosen kitchen sink.
        :return: Returns chosen kitchen sink as type Feature.
        """
        return self.kcounter

    def set_fridge(self):
        """
        This function sets the fridge attribute after prompting user for input from set menu.
        """
        while True:
            print("\nWhat kind of fridge do you want?")
            index = 1
            for fridge in fridges:  # Creates menu of fridges to choose from.
                print(index, "-", fridge)
                index += 1
            choice = input('Enter the corresponding number of your choice from the menu above: ')
            try:
                choice = int(choice)
            except:
                print("This is not a valid entry! Enter a number.\n")
                continue
            if choice == 1 or choice == 2 or choice == 3:
                break
            else:
                print("This is not a valid entry! Number must match a menu item.\n")
        self.attributes['fridge'] = fridges[choice - 1]
        self.fridge = fridges[choice - 1]
        self.fridge.count = 1

    def get_fridge(self):
        """
        This function returns the chosen fridge.
        :return: Returns chosen fridge as type Feature.
        """
        return self.fridge

    def set_sink(self):
        """
        This function sets the fridge attribute after prompting user for input from set menu.
        """
        print("")
        while True:
            index = 1
            print("What kind of kitchen sink do you want?")
            for sink in kitchen_sinks:  # Creates menu of sinks to choose from.
                print(index, "-", sink)
                index += 1
            choice = input('Enter the corresponding number of your choice from the menu above: ')
            try:
                choice = int(choice)
            except:
                print("This is not a valid entry! Must enter a number.\n")
                continue
            if choice == 1 or choice == 2:
                break
            else:
                print("This is not a valid entry! Number must match a menu item.\n")
        self.attributes['sink'] = kitchen_sinks[choice - 1]
        self.sink = kitchen_sinks[choice - 1]
        self.sink.count = 1

    def get_sink(self):
        """
        This function returns the chosen sink.
        :return: Returns chosen sink as type Feature.
        """
        return self.sink