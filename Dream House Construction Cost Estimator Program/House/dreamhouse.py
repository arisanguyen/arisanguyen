"""
This module contains the class DreamHouse. To help run this module, the Feature, Room, Kitchen, and Bathroom modules
will be imported here.
"""

# Modules to import.

from House.feature import Feature
from House.room import Room
from House.kitchen import Kitchen
from House.bathroom import Bathroom

# List of possible house attributes to choose from.

locations = {'blank': 1, 'ANCHORAGE': 1.029, 'PHOENIX': 1.031, 'SAN FRANCISCO': 1.039, 'DENVER': 1.036,
                 'MIAMI': 1.030, 'HONOLULU': 1.021, 'CHICAGO': 1.023, 'BOSTON': 1.025, 'NEW YORK CITY': 1.023,
                 'AUSTIN': 1.033, 'SEATTLE': 1.044}  # Citation: (Gordian, 2019)

flooring_default = Feature('blank', 0, 'sqft')
flooring1 = Feature('Hardwood flooring', 7, 'sqft')  # Citation: (Twenty & Oak)
flooring2 = Feature('Tile flooring', 4, 'sqft')  # Citation: (Twenty & Oak)
flooring3 = Feature('Vinyl flooring', 3, 'sqft')  # Citation: (Twenty & Oak)
floorings = [flooring1, flooring2, flooring3]

roofing_default = Feature('Blank', 0, 'sqft')
roofing1 = Feature('Slate', 20, 'sqft')  # Citation: (HomeAdvisor, Inc., 2021)
roofing2 = Feature('Asphalt shingles', 3, 'sqft')  # Citation: (Modernize, 2021)
roofings = [roofing1, roofing2]

sqft_default = Feature('Sqft', 100, 'sqft')  # Citation: (Liasison Ventures, Inc.)

flr_default = Feature('Floor', 100, 'sqft')  # Citation: (Liasison Ventures, Inc.)

bedroom_default = Room(0, 0, 15000, 'bedroom')  # Citation: (Liasison Ventures, Inc.)

kitchen_default = Kitchen()
kitchen_default.count = 1
kitchen_default.basecost = 35000  # Citation: (Liasison Ventures, Inc.)

bathroom_default = Bathroom()
bathroom_default.basecost = 35000  # Citation: (Liasison Ventures, Inc.)

class DreamHouse():
    """
    This class stores all information about the user's dream house. It also calculates the total cost of the house and
    returns a summary.
    """

    def __init__(self, sqft = sqft_default, flr = flr_default, bedroom = bedroom_default, roofing = roofing_default, flooring = flooring_default, kitchen = kitchen_default, bathroom = bathroom_default):
        """
        This function initializes the DreamHouse class.
        :param sqft: This should be entered as type Feature and refers to the square footage of the house.
        :param flr: This should be entered as type Feature and refers to the number of floors.
        :param bedroom: This should be entered as type Room and refers to the bedroom and its features.
        :param roofing: This should be entered as type Feature and refers to the roofing material.
        :param flooring: This should be entered as type Feature and refers to the flooring material.
        :param kitchen: This should be entered as type Kitchen and refers to the kitchen and its features.
        :param bathroom: This should be entered as type Bathroom and refers to the bathroom and its features.
        """
        self.sqft = sqft
        self.floors = flr
        self.floor_num = 0
        self.bedroom = bedroom
        self.roofing = roofing
        self.flooring = flooring
        self.kitchen = kitchen
        self.bathroom = bathroom
        self.location = 'blank'
        self.cost = 0

    def summary(self):
        """
        This function returns a summary of the uesr's dream house as a string.
        :return: Summary of house as string.
        """
        print(f"Your house costs ${self.total_cost():,.2f}, is {self.sqft.count} sqft, contains {self.floor_num} floor(s) with {self.bedroom.count} bedroom(s), and located in {self.location.title()}.")
        print(f"Your house also has {self.flooring.name.lower()} and your roof is made of {self.roofing.name.lower()}.")
        print(f"Your kitchen costs ${self.kitchen.total_cost():,.2f} and contains a {self.kitchen.kcounter.name.lower()} countertop, {self.kitchen.fridge.name.lower()}, and {self.kitchen.sink.name.lower()}.")
        if self.bathroom.count == 1:
            print(f"Your {self.bathroom.count} bathroom costs ${self.bathroom.total_cost():,.2f} and contains a {self.bathroom.bcounter.name.lower()} countertop, and {self.bathroom.shower.name.lower()}.")
        else:
            print(f"Your {self.bathroom.count} bathrooms cost ${self.bathroom.total_cost():,.2f} and contain {self.bathroom.bcounter.name.lower()} countertops and {self.bathroom.shower.name.lower()}s.")

    def total_cost(self):
        """
        This function calculates and updates the self.cost of the house.
        :return: Returns total cost of house as numeric.
        """
        self.cost = 0
        self.cost += self.sqft.total_cost()
        self.cost += self.floors.total_cost()
        self.cost += self.bedroom.total_cost()
        self.cost += self.roofing.total_cost()
        self.cost += self.flooring.total_cost()
        self.cost += self.kitchen.total_cost()
        self.cost += self.bathroom.total_cost()
        self.cost *= locations[self.location]  # Multiplying the total cost of the house by the location multiplier.
        return self.cost

    def set_location(self):
        """
        This function sets the location of the house by prompting the user for input from set menu.
        """
        while True:
            print('\nBelow are the cities you can build your house in.')
            for loc in locations:  # Creates menu of locations to choose from.
                if loc == 'blank':
                    continue
                else:
                    print(loc.title())
            choice = input("Please choose the a city from the menu above and enter it here: ")
            if str(choice).upper() in locations and str(choice) != 'blank':
                self.location = str(choice).upper()
                break
            else:
                print('This is not a valid entry (must be from the menu)!')

    def get_location(self):
        """
        :return: This function returns location as string.
        """
        return self.location

    def set_sqft(self):
        """
        This function sets the square footage of the house by prompting the user for input.
        """
        print("")
        while True:
            choice = input('How many total square feet would you like your house to be? You can choose a positive whole number between 500 and 10,000 sqft: ')
            try:
                choice = int(choice)
            except:
                print('This is not a valid entry! Must enter a number!\n')
                continue
            if 10000 >= choice >= 500:
                break
            else:
                print('This is not a valid entry! Must enter a number between 500 and 10,000, inclusive.\n')
        self.sqft.count = choice

    def get_sqft(self):
        """
        :return: This function returns square footage as numeric.
        """
        return self.sqft

    def set_floors(self):
        """
        This function sets the number of floors of the house by prompting the user for input from set menu.
        """
        print("")
        while True:
            choice = input('How many floors would you like your house to be? You can choose 1 or 2 floors: ')
            try:
                choice = int(choice)
            except:
                print('This is not a valid entry! Must enter a number!\n')
                continue
            if choice == 1 or choice == 2:
                break
            else:
                print('This is not a valid entry! Must choose 1 or 2!\n')
        self.floor_num = choice
        self.floors.count = (choice - 1) * (self.sqft.count // 2)

    def get_floors(self):
        """
        :return: This function returns number of floors as type Feature.
        """
        return self.floors

    def set_bedroom(self):
        """
        This function sets the number of bedrooms of the house by prompting the user.
        """
        print("")
        while True:
            choice = input('How many bedrooms would you like? Enter a reasonable number between 1 and 20: ')
            try:
                choice = int(choice)
            except:
                print('This is not a valid answer! Must enter a number!\n')
                continue
            if 1 <= choice <= 20:
                break
            else:
                print('This is not a valid answer! Must enter a number between 1 and 20, inclusive.\n')
        self.bedroom.count = choice

    def get_bedroom(self):
        """
        :return: This function returns bedroom as type Room.
        """
        return self.bedroom

    def set_roofing(self):
        """
        This function sets the roofing material type of the house by prompting the user for input from set menu.
        """
        print("")
        while True:
            index = 1
            print('What kind of material would you like your roof to be made of?')
            for roof in roofings:  # Creates a menu of roofing material to choose from.
                print(index, "-", roof)
                index += 1
            choice = input('Please enter the corresponding number of your choice from the menu above: ')
            try:
                choice = int(choice)
            except:
                print('This is not a valid answer! Enter a number. \n')
                continue
            if choice == 1 or choice == 2:
                break
            else:
                print('This is not a valid answer! Number must match a menu item.\n')
        self.roofing = roofings[choice - 1]
        self.roofing.count = float(self.sqft.count) // float(self.floor_num)

    def get_roofing(self):
        """
        :return: This function returns roofing as type Feature.
        """
        return self.roofing

    def set_flooring(self):
        """
        This function sets the flooring type of the house by prompting the user for input from set menu.
        """
        print("")
        while True:
            index = 1
            print('What kind of flooring would you like throughout your house?')
            for flooring in floorings:  # Creates menu of flooring type to choose from.
                print(index, "-", flooring)
                index += 1
            choice = input('Please enter the corresponding number of your choice from the menu above: ')
            try:
                choice = int(choice)
            except:
                print("This is not a valid entry! Must enter a number.\n")
                continue
            if choice == 1 or choice == 2 or choice == 3:
                break
            else:
                print('This is not a valid answer! Number must match a menu item.\n')
        self.flooring = floorings[choice - 1]
        self.flooring.count = self.sqft.count

    def get_flooring(self):
        """
        :return: This function returns flooring as type Feature.
        """
        return self.flooring

    def set_kitchen(self):
        """
        This function sets the kitchen attributes of the house.
        """
        self.kitchen.set_kcounter()  # This prompts the user to set kitchen counter attribute.
        self.kitchen.set_sink()  # This prompts the user to set sink attribute.
        self.kitchen.set_fridge()  # This prompts the user to set fridge attribute.

    def get_kitchen(self):
        """
        :return: This function returns kitchen as type Kitchen.
        """
        return self.kitchen

    def set_bathroom(self):
        """
        This function sets the bathroom count and attributes of the house.
        """
        print("")
        while True:
            choice = input('How many bathrooms would you like? Enter a reasonable number between 1 and 20: ')
            try:
                choice = int(choice)
            except:
                print('This is not a valid answer! Must enter a number.\n')
                continue
            if 1 <= choice <= 20:
                break
            else:
                print('This is not a valid answer! Must enter a number between 1 and 20, inclusive.\n')
        self.bathroom.count = choice
        self.bathroom.set_bcounter()  # This prompts use to set bathroom counter attribute.
        self.bathroom.set_shower()  # This prompts user to set shower/ bathtub attribute.

    def get_bathroom(self):
        """
        :return: This function returns kitchen as type Bathroom.
        """
        return self.bathroom

    def __str__(self):
        """
        :return: House cost as string.
        """
        return f"Your dream house costs {self.total_cost()}."

    def __repr__(self):
        """
        :return: House cost as string.
        """
        return self.__str__()