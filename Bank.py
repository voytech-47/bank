class Bank:
    _accounts = []
    _peopleID = {
        "people": [],
        "bankers": []
    }
    _name = None
    _capital = None

    def __init__(self, name):
        self.setBankName(name)
        self._capital = None

    def setBankName(self, name):
        self._name = name

    def getBankName(self):
        return self._name

    def setCapital(self, value):
        self._capital = value

    def getCapital(self):
        return self._capital

    def changeCapital(self, value):
        self.getCapital() + value

    def getIds(self):
        return self._peopleID

    def addId(self, person):
        self._peopleID["people"].append(person)

    def deleteId(self, id):
        self.getIds()["people"].remove(id)

    def addAccount(self, account, id):
        self.addId(id)
        self._accounts.append(account)

    def getAccounts(self):
        return self._accounts

    def deleteAccount(self, account):
        self.deleteId(account.getID())
        account.getOwner().deleteAccount(account)
        self.changeCapital(-account.getBalance())
        self._accounts.remove(account)

    def _hireBanker(self, banker):
        banker.setBank(self)
        self._peopleID["bankers"].append(banker)
