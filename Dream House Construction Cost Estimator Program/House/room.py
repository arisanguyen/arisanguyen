"""
This module contains the class Room. It is the superclass to the subclasses Kitchen and Bathroom.
"""

class Room():
    """
    This class is the superclass to Kitchen and Bathroom. It holds the Room object and also returns a summary.
    """

    def __init__(self, count = 0, cost = 0, basecost = 0, type = "blank"):
        """
        This is the initializer function to Room.
        :param count: This input should be of type integer. It refers to the count of a particular room type.
        :param cost: This input should be of tupe numeric. It refers to the total cost of the room, and is updated
            via the total_cost function.
        :param basecost: This input should be of type numeric. It refers to the basecost to build one room.
        :param type: This input should be of type string. It refers to the type of room (eg. bedroom, bathroom, etc).
        """
        self.count = count  # count of that particular number of rooms
        self.cost = cost  # starting cost should be 0
        self.basecost = basecost
        self.attributes = {}  # dictionary containing all features of a room
        self.type = type

    def total_cost(self):
        """
        This function adds up the total cost of all the rooms of one type (eg. all the bedrooms) and updates
            the self.cost attribute.
        :return: Returns the total cost of the room(s).
        """
        values = list(self.attributes.values())
        self.cost = 0
        for att in values:  # Adding up the total cost of attributes (eg. sink, fridge).
            self.cost += (att.total_cost() * self.count)
        self.cost += (self.basecost * self.count)  # Adding in the basecost of each room.
        return self.cost

    def __str__(self):
        """
        :return: Returns cost summary via string.
        """
        return f"This is your {self.type} which costs {self.total_cost()}."

    def __repr__(self):
        """
        :return: Returns cost summary via string.
        """
        return self.__str__()