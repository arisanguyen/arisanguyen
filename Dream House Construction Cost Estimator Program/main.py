"""
Program: Dream House Construction Cost Estimator
Developer: Arisa Nguyen

This is the main file that the Dream House Construction Cost Estimator program runs from. This program is used to help
estimate the construction costs of the user's dream house. Please enter this file into the command line to run the program.

The other files needed with this program are compare.py, budget.py, and the House package which contains dreamhouse.py,
bathroom.py, kitchen.py, room.py, and feature.py.
"""

# Importing necessary packages and modules.

from House.dreamhouse import DreamHouse
# The House package being use to importing DreamHouse contains DreamHouse (class #1), Room (class #2), Kitchen
# (class #3), Bathroom (class #4), and Feature (class #5) modules/ classes.They all work with each other on the backend.
# For this main file, only DreamHouse class is needed from the House package.
from budget import Budget  # Class 6 - Class that helps manage user's budget
from compare import Compare  # Class 7 - Class to compare the house before and after changes made.
import copy

# Function to help run the main function.

def pause():
    """
    This function adds a pausing feature to give user time to read instructions. Ensures user enters valid response.
    """
    valid = False
    while valid == False:
        choice = input('Enter the letter N to continue: ')
        choice = str(choice).lower()
        if choice == "n":
            valid = True
        else:
            print("Invalid entry!\n")

# MAIN CODE that prompts user with instructions.

def main():
    """
    This function runs the main code for the program.
    """

    print ('\nWelcome to the Dream House Construction Cost Estimator!'
           '\nThis program will ask you to choose attributes about your dream house. Then it will estimate the total construction cost.'
           '\n'
           '\nFirst we will start with basic information about your dream house.\n')

    pause()  # Creates a pause so that user can read the initial instructions.

    house = DreamHouse()  # Creating the default dream house to work off of.

    house.set_location()  # Prompts user for location.

    house.set_sqft()  # Prompts user for desired square footage.

    house.set_floors()  # Prompts user for number of floors.

    house.set_bedroom()  # Prompts user for number of bedrooms.

    house.set_flooring()  # Prompts user for flooring type throughout house.

    house.set_roofing()  # Prompts user for roofing material type.

    print("\nGreat! Now let's fill in some information about the bathroom.")
    print(f"Just so you know, the base cost per bathroom is ${house.bathroom.basecost:,.2f}.\n")

    pause()  # Creates a pause so that user can read the instructions.

    house.set_bathroom()  # Prompts user to choose bathroom count and its attributes.

    print("\nOkay, now let's get more specific information about your kitchen.")
    print(f"Just so you know, the base cost for one kitchen is ${house.kitchen.basecost:,.2f}.\n")

    pause()  # Creates a pause so that user can read the instructions.

    house.set_kitchen()  # Prompts user to choose kitchen attributes.

    print('\nAwesome! Thanks for that information. One last step before I show you the total cost.')

    while True:
        budget = Budget(house)  # Creating a default budget for house to work off of.
        choice = input('\nDo you have a budget you want to compare the total cost to? Please enter YES or NO: ')
        if str(choice).lower() == 'yes':
            budget.set_budget()  # Prompts user to set budget.
            break
        elif str(choice).lower() == 'no':
            break
        else:
            print("Not a valid entry! Must enter YES or NO.")

    print("\nReady to see your summary?\n")

    pause()

    print("\n*****************SUMMARY*****************")
    house.summary()  # Prints cost and attributes summary of the house.
    budget.summary()  # Prints summary of how budget compares to house cost.
    print("*****************************************")

    while True:
        choice = input("\nDo you want to make changes to your house? Enter YES or NO: ")
        if str(choice).lower() != "yes" and str(choice).lower() != "no":
            print('This is not a valid entry! Must enter YES or NO.')
        else:
            break

    while True:
        if str(choice).lower() == "yes":  # User wants to make changes to their house.
            house_initial = copy.deepcopy(house)  # Creating a before-changes version of house to compare later to after-changes version.
            while True:
                print('\nWhat do you want to change? \nBathroom \nKitchen \nBedroom \nSomething else')
                choice = input("Choose and enter one of the categories above: ")
                choice = str(choice).lower()
                if choice == 'bathroom':
                    house.set_bathroom()  # Prompts user to change bathroom.
                elif choice == 'kitchen':
                    house.set_kitchen()  # Prompts user to change kitchen.
                elif choice == 'bedroom':
                    house.set_bedroom()  # Prompts user to change bedroom.
                elif choice == 'something else':
                    while True:
                        print("\nWhat do you want to change? \nSquare footage \nNumber of floors \nLocation \nFlooring \nRoofing \nBudget")
                        attribute = input('Choose and enter the attribute you want to change from the menu above: ')
                        if str(attribute).lower() == 'square footage':
                            house.set_sqft()  # Prompts user to change square footage.
                        elif str(attribute).lower() == 'number of floors':
                            house.set_floors()  # Prompts user to change number of floors.
                        elif str(attribute).lower() == 'location':
                            house.set_location()  # Prompts user to change location.
                        elif str(attribute).lower() == 'flooring':
                            house.set_flooring()  # Prompts user to change flooring type.
                        elif str(attribute).lower() == 'roofing':
                            house.set_roofing()  # Prompts user to change roofing type.
                        elif str(attribute).lower() == 'budget':
                            print(f"\nYour budget is currently: ", budget)
                            while True:
                                choice = input("Do you want to increase or decrease your budget? ")
                                if str(choice).lower() == 'increase':
                                    budget.increase()  # Prompts user to increase budget.
                                elif str(choice).lower() == 'decrease':
                                    budget.decrease()  # Prompts user to decrease budget.
                                else:
                                    print("Not a valid entry! Must enter INCREASE or DECREASE.\n")
                                    continue
                                break
                        else:
                            print("This is not a valid entry! Must enter SQUARE FOOTAGE, NUMBER OF FLOORS, LOCATION, FLOORING, ROOFING,or BUDGET.")
                        break
                else:
                    print('Not a valid entry! Must enter KITCHEN, BATHROOM, BEDROOM, or SOMETHING ELSE.')
                    continue
                while True:
                    choice = input("\nDo you want to make more changes to your house? Enter YES OR NO: ")
                    if str(choice).lower() == 'yes' or str(choice).lower() == 'no':
                        break
                    else:
                        print("Not a valid entry! Must enter YES or NO.")
                if str(choice).lower() == 'no':  # Breaks if user does not want to make any further changes to house.
                    break
        elif choice == 'no':  # User does not or is done making changes, and program ends.
            print('\nThis is the end of the Dream House Cost Estimator! Thank you for using me! Goodbye!')
            break

        compare = Compare(house_initial, house)  # To compare the house before and after changes.

        print("\n*****************SUMMARY*****************")
        compare.summary()  # Prints cost summary of changes made to house.
        house.summary()  # Prints cost and attributes summary of the house.
        budget.summary()  # Prints summary of how budget compares to house cost.
        print("*****************************************")

if __name__ == "__main__":  # Runs the main function.
    main()