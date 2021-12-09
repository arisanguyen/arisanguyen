"""
This module contains the class Compare.
"""

class Compare():
    """
    This class has functions that help compare the cost of the user's house before and after their changes.
    """

    def __init__(self, dreamhouse1, dreamhouse2):
        """
        This function initializes the Compare class.
        :param dreamhouse1: This should be inputted as type DreamHouse, and refers to the house before changes.
        :param dreamhouse2: This should be inputted as type DreamHouse, and refers to the house after changes.
        """
        self.house1 = dreamhouse1
        self.house2 = dreamhouse2

    def summary(self):
        """
        :return: This function returns a cost summary of changes as a string.
        """
        if self.total_diff() > 0:  # Evaluating difference in total cost
            amount = abs(self.total_diff())
            str = f"After your changes, the total cost of your house decreased by ${amount:,.2f}, "
        elif self.total_diff() < 0:
            amount = abs(self.total_diff())
            str = f"After your changes, the total cost of your house increased by ${amount:,.2f}, "
        else:
            str = "After your changes, the overall cost of your house didn't change, "
        if self.kitchen_diff() > 0:  # Evaluating different in kitchen cost
            amount = abs(self.kitchen_diff())
            str2 = f"your kitchen costs decreased by ${amount:,.2f}, "
            str = str + str2
        elif self.kitchen_diff() < 0:
            amount = abs(self.kitchen_diff())
            str2 = f"your kitchen costs increased by ${amount:,.2f}, "
            str = str + str2
        else:
            str2 = f"your kitchen costs didn't change, "
            str = str + str2
        if self.bathroom_diff() > 0:  # Evaluating difference in bathroom cost
            amount = abs(self.bathroom_diff())
            str2 = f"and your bathroom costs decreased by ${amount:,.2f}."
            str = str + str2
        elif self.bathroom_diff() < 0:
            amount = abs(self.bathroom_diff())
            str2 = f"and your bathroom costs increased by ${amount:,.2f}."
            str = str + str2
        else:
            str2 = f"and your bathroom costs didn't change."
            str = str + str2
        print(str)

    def total_diff(self):
        """
        This function calculates the total cost difference after changes.
        :return: Returns the difference in cost as numeric.
        """
        diff = self.house1.total_cost() - self.house2.total_cost()
        return diff

    def kitchen_diff(self):
        """
        This function calculates the kitchen cost difference after changes.
        :return: Returns the difference in cost as numeric.
        """
        diff = self.house1.kitchen.total_cost() - self.house2.kitchen.total_cost()
        return diff

    def bathroom_diff(self):
        """
        This function calculates the bathroom cost difference after changes.
        :return: Returns the difference in cost as numeric.
        """
        diff = self.house1.bathroom.total_cost() - self.house2.bathroom.total_cost()
        return diff

