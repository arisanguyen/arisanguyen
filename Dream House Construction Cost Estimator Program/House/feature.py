"""
This module contains the class Feature. This module is used in the bathroom, kitchen, and dreamhouse modules.
"""

class Feature():
    """
    This class holds the Feature object and its associated name, count, cost, and total cost.
    """

    def __init__(self, name, cost_per, unit, count = 0):
        """
        This function initializes the Feature class.
        :param name: This should be entered as a string, and refers to the name of the feature (eg. double sink).
        :param cost_per: This should be entered as a numeric, and refers to the cost per unit.
        :param unit: This should be entered as a string, and refers to the unit measurement type (eg. unit, sqft).
        :param count: This should be entered as an integer, and refers to the count of the feature.
        """
        self.name = name  # name of feature (eg. double sink, hardwood floor)
        self.cost_per = cost_per  # cost per unit
        self.unit = unit  # unit type used (eg. unit, sqft)
        self.count = count  # total count of this feature in units named in self.unit
        self.cost = 0  # total cost of feature after multiplying cost_per and count using function total_cost

    def total_cost(self):
        """
        This function adds up the total cost of the feature by multiplying the cost_per and count, then updates the
            self.cost attribute.
        :return: Returns the total cost of the feature.
        """
        self.cost = (self.cost_per * self.count)
        return self.cost

    def __str__(self):
        """
        :return: Returns feature as a string with feature name, cost per, and unit type.
        """
        return f"{self.name} at ${self.cost_per:,} per {self.unit}"

    def __repr__(self):
        """
        :return: Returns feature as a string with feature name, cost per, and unit type.
        """
        return self.__str__()
