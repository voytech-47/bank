from datetime import date

from Operation import Operation


class Account:
    _owner = None
    _id = None
    _balance = 0.0
    _max_debit = 100.0
    _operations = []
    _currency = None

    def __init__(self, currency, owner, id):
        self.setCurrency(currency)
        self.setOwner(owner)
        self.setId(id)

    def setOwner(self, owner):
        self._owner = owner

    def getOwner(self):
        return self._owner

    def setId(self, id):
        self._id = id

    def getId(self):
        return self._id

    def setCurrency(self, currency):
        self._currency = currency

    def getCurrency(self):
        return self._currency

    def getBalance(self):
        return self._balance

    def changeBalance(self, amount, ):
        self.checkDebit(amount)
        self.createOperation("wypłata" if amount < 0 else "wpłata", amount, )
        self._balance += amount

    def getDebit(self):
        return self._max_debit

    def checkDebit(self, amount):
        if self.getBalance() + amount < -self.getDebit():
            raise Exception("Debit exceeded!")

    def addOperation(self, operation):
        self._operations.append(operation)

    def incomingTransfer(self, amount, sender, title='Work payment'):
        self.createOperation('Incoming transfer', amount, sender, title)

    def outgoingTransfer(self, amount, recipient, title='Money transfer'):
        self.createOperation('Outgoing transfer', amount, recipient, title)

    def withdraw(self, amount):
        if abs(amount) > self.getBalance() + self.getDebit():
            raise Exception("Not enough money!")
        if abs(amount) > self.getBalance():
            print("You're in debt!")
        self.changeBalance(-amount)
        print(f"Withdrawal successful, balance: {self.getBalance()} {self.getCurrency()}")

    def deposit(self, amount):
        if not (amount % 10):
            raise Exception("Deposit must be a multiple of 10")
        self.createOperation("Deposit", amount, self, "Deposit at an ATM")

    def createOperation(self, type, amount, person, title):
        operation = Operation(type, amount, person, title, date.today())
        self.addOperation(operation)

    def getOperations(self):
        return self._operations
