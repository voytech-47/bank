class Operation:
    _operationTypes = None
    _amount = None
    _person = None
    _title = None
    _date = None

    def __init__(self, type, amount, person, title, date):
        self.setOperationType(type)
        self.setAmount(amount)
        self.setPerson(person)
        self.setTitle(title)
        self.setDate(date)

    def getDate(self):
        return self._date

    def setDate(self, value):
        self._date = value

    def getTitle(self):
        return self._title

    def setTitle(self, title):
        self._title = title

    def getPerson(self):
        return self._person

    def setPerson(self, value):
        self._person = value

    def getOperationType(self):
        return self._operationTypes

    def setOperationType(self, value):
        self._operationTypes = value

    def getAmount(self):
        return self._amount

    def setAmount(self, value):
        self._amount = value

    def __str__(self):
        return f"Operation type: {self.getOperationType()}\nAmount: {self.getAmount()}\nAccount: {self.getPerson()}, \nDate: {self.getDate()}"
