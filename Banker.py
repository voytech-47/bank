import random

from Account import Account
from Person import Person


class Banker(Person):
    _bank = None

    def __init__(self, name, surname, currency):
        super().__init__(name, surname, currency)

    def setBank(self, bank):
        self._bank = bank

    def getBank(self):
        return self._bank

    def openAccount(self, person):
        newID = random.randint(1, 999)
        while newID in self.getBank().getIds():
            newID = random.randint(1, 999)
        person.addAccount(self.getBank().getBankName(), newID)
        account = Account(person.getCurrency(), person, newID)
        self.getBank().addAccount(account, newID)
        return account

    def closeAccount(self, account):
        self.getBank().deleteAccount(account)
