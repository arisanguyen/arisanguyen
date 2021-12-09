"""
This module contains the class Budget.
"""

class Budget():
    """
    This class stores information about the user's budget, as well as perform functions on the budget.
    """

    def __init__(self, dreamhouse, budget = 0):
        """
        This function initializes the Budget class.
        :param dreamhouse: This should be inputted as type DreamHouse and refers to the user's constructed house.
        :param budget: This should be inputted as a numeric and refers to the user's budget.
        """
        self.house = dreamhouse
        self.budget = budget

    def summary(self):
        """
        This function returns a summary of the budget compared to the cost of the user's house.
        :return: Summary of budget compared to house as string.
        """
        if self.budget == 0:
            print("You did not enter a budget for this house.")
        elif self.house.total_cost() > self.budget:
            diff = self.house.total_cost() - self.budget
            print(f"Oh no! Your house costs ${diff:,.2f} more than your budget of ${self.budget:,.2f}.")
        elif self.house.total_cost() < self.budget:
            diff = self.budget - self.house.total_cost()
            print(f"Hooray! Your house costs ${diff:,.2f} less than your budget of ${self.budget:,.2f}.")
        elif self.house.total_cost() == self.budget:
            print(f"Wow! You house will cost the same as your budget!")

    def set_budget(self):
        """
        This function sets the user's budget by prompting user.
        """
        while True:
            budg = input('\nWhat is your budget? Enter a positive number greater than 0: ')
            try:
                budg = float(budg)
            except:
                print("This is not a valid entry! Must enter a number!\n")
                continue
            if budg > 0:
                self.budget = budg
                break
            else:
                print("This is not a valid entry! Must enter a positive number greater than 0.\n")

    def get_budget(self):
        """
        :return: This returns the budget as a numeric.
        """
        return self.budget

    def increase(self):
        """
        This function increases the user's budget by prompting user.
        """
        while True:
            amount = input("\nHow much do you want to increase your budget by? Enter a positive number: ")
            try:
                amount = float(amount)
            except:
                print("Not a valid entry! Must enter a number!")
                continue
            if amount < 0:
                print("Not a valid entry! Must enter a number greater than 0.")
            else:
                break
        self.budget += amount

    def decrease(self):
        """
        This function decreases the user's budget by prompting user. It ensures that the budget stays above $0.
        """
        while True:
            amount = input("\nHow much do you want to decrease your budget by? Enter a positive number: ")
            try:
                amount = float(amount)
            except:
                print("Not a valid entry! Must enter a number!")
                continue
            if amount < 0:
                print("Not a valid entry! Must enter a number greater than 0.")
                continue
            if self.budget < amount:
                print("Impossible! Decrease amount exceeds your current budget! Enter a smaller number.")
            elif self.budget == amount:
                print("Not possible! This would make your budget $0. Budgets must be >$0. Enter a smaller number.")
            else:
                self.budget -= amount
                break

    def __str__(self):
        """
        :return: Returns budget. If no budget entered in the first place, it will return No Budget Entered.
        """
        if self.budget == None:
            str = 'No Budget Entered'
        else:
            str = f'${self.budget:,.2f}'
        return str

    def __repr__(self):
        """
        :return: Returns budget. If no budget entered in the first place, it will return No Budget Entered.
        """
        self.__str__()