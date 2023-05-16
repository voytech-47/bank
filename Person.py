import re


class Person:
    _name = None
    _surname = None
    _accounts = []
    _currency = None

    def __init__(self, name, surname, currency):
        self.setName(name)
        self.setSurname(surname)
        self.setCurrency(currency)

    def setName(self, name):
        self._name = self._validateInput(name)

    def getName(self):
        return self._name

    def setSurname(self, surname):
        self._surname = self._validateInput(surname)

    def getSurname(self):
        return self._surname

    def addAccount(self, bank, id):
        self._accounts.append((bank, id))

    def getAccounts(self):
        return self._accounts

    def deleteAccount(self, account):
        self.getAccounts().remove(account)

    def getFullName(self):
        return f"{self._name} {self._surname}"

    def setCurrency(self, currency):
        self._currency = currency

    def getCurrency(self):
        return self._currency

    @staticmethod
    def _validateInput(input_value):
        flag = re.search("^[a-zA-ZżźćńółęąśŻŹĆĄŚĘŁÓŃ]+$", input_value)
        if flag:
            return input_value.capitalize()
        else:
            raise Exception("Incorrect input!")
