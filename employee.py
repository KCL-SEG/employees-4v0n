"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

import string


class Contract:
    def __init__(self, wage: int):
        self.type = type
        self.wage = wage

    def get_wage(self):
        return self.wage

    def __str__(self):
        return "salary of " + str(self.wage)

class HourlyContract(Contract):
    def __init__(self, wage: int, hoursWorked: int):
        super().__init__(wage)
        self.hoursWorked = hoursWorked

    def get_wage(self):
        return (self.wage * self.hoursWorked)

    def __str__(self):
        return "contract of " + str(self.hoursWorked) + " hours at " + str(self.wage) + "/hour"
        
class MonthlyContract(Contract):
    def __init__(self, wage: int):
        super().__init__(wage)

    def __str__(self):
        return "monthly " + super().__str__()

class Commission:
    def __init__(self, amount: int):
        self.amount = amount

    def get_commission(self):
        return self.amount

    def __str__(self):
        return " and receives a "
        
class NoCommission(Commission):
    def __init__(self):
        super().__init__(0)

    def __str__(self):
        return ""

class BonusCommission(Commission):
    def __init__(self, amount: int):
        super().__init__(amount)

    def __str__(self):
        return super().__str__() + "bonus commission of " + str(self.amount)

class ContractCommission(Commission):
    def __init__(self, commission_per_contract: int, contracts_landed: int):
        super().__init__(commission_per_contract)
        self.contracts_landed = contracts_landed

    def get_commission(self):
        return (self.amount * self.contracts_landed)

    def __str__(self):
        return super().__str__() + "commission for " + str(self.contracts_landed) + " contract(s) at " + str(self.amount) + "/contract"

class Employee:
    def __init__(self, name: str, contract: Contract, commission: Commission):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        return (self.contract.get_wage() + self.commission.get_commission())

    def __str__(self):
        return self.name + " works on a " + str(self.contract) + str(self.commission) + ". Their total pay is " + str(self.get_pay()) + "."

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', MonthlyContract(4000), NoCommission())

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyContract(25, 100), NoCommission())

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlyContract(3000), ContractCommission(200, 4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyContract(25,150), ContractCommission(220, 3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlyContract(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyContract(30,120), BonusCommission(600))