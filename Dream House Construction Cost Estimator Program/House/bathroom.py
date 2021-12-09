"""
This module contains the class Bathroom. To help this module run, room and feature modules are imported here.
"""

# Modules to import.

from House.room import Room
from House.feature import Feature

# List of possible bathroom attributes to choose from.

default_counter = Feature('blank', 0, 'counter')
counter1 = Feature('Granite', 3000, 'counter')  # Citation: (Thompson, 2021)
counter2 = Feature('Quartz', 4000, 'counter')  # Citation: (Thompson, 2021)
counter3 = Feature('Plastic laminate', 1000, 'counter')  # Citation: (HomeAdvisor, ...counter...)
counters = [counter1, counter2, counter3]

default_shower = Feature('blank', 0, 'unit')
shower1 = Feature('Bathtub', 4000, 'unit')  # Citation: (HomeAdvisor, ...bathtub...)
shower2 = Feature('Shower', 1500, 'unit')  # Citation: (Homewyse, 2021)
showers = [shower1, shower2]

class Bathroom(Room):
    """
    This class is a subclass of Room. It holds the Bathroom object and also prompts user to choose bathroom attributes.
    """

    def __init__(self, counter = default_counter, shower = default_shower):
        """
        This is the initializer function for Bathroom.
        :param counter: This input should be of type Feature, and refers to the chosen counter.
        :param shower: This input should be of type Feature, and refers to the chosen shower/bathtub.
        """
        super().__init__()
        self.counter = counter
        self.shower = shower
        self.type = 'bathroom'

    def set_bcounter(self):
        """
        This function sets the bathroom counter attribute after prompting user for input from set menu.
        """
        print("")
        while True:
            index = 1
            print("What kind of material do you want your bathroom countertop to be made of?")
            for counter in counters:
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
        self.attributes['bcounter'] = counters[choice - 1]
        self.bcounter = counters[choice - 1]
        self.bcounter.count = 1

    def get_bcounter(self):
        """
        This function returns the chosen bathroom counter.
        :return: Returns chosen bathroom counter as type Feature.
        """
        return self.bcounter

    def set_shower(self):
        """
        This function sets the shower/bathtub attribute after prompting user for input from set menu.
        """
        print("")
        while True:
            index = 1
            print("Do you want a shower or bathtub?")
            for shower in showers:
                print(index, "-", shower)
                index += 1
            choice = input('Enter the corresponding number of your choice from the menu above: ')
            try:
                choice = int(choice)
            except:
                print("This is not a valid entry! Enter a number.\n")
                continue
            if choice == 1 or choice == 2:
                break
            else:
                print("This is not a valid entry! Number must correspond to a menu item.\n")
        self.attributes['shower'] = showers[choice - 1]
        self.shower = showers[choice - 1]
        self.shower.count = 1

    def get_shower(self):
        """
        This function returns the chosen shower/ bathtub.
        :return: Returns chosen shower/ bathtub as type Feature.
        """
        return self.shower