from Person import Person


class Boss(Person):
    _bank = None

    def __init__(self, name, surname, currency, bank):
        super().__init__(name, surname, currency)
        self.setBank(bank)

    def getBank(self):
        return self._bank

    def setBank(self, value):
        self._bank = value

    def hireBanker(self, banker):
        self.getBank()._hireBanker(banker)