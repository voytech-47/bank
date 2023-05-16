from Boss import Boss
from Bank import Bank
from Banker import Banker
from Person import Person

mbank = Bank('mBank')
ludzik = Person('adam', "KOWALSKI", 'ZŁ')
czlowiek = Person('jan', 'nowak', 'ZŁ')
kierwonik = Banker('bożena', 'nowak', 'ZŁ')
admin = Boss('wojciech', 'grzybowski', 'ZŁ', mbank)

admin.hireBanker(kierwonik)
konta = kierwonik.getBank().getAccounts()
print(konta)
czlowiek_konto = kierwonik.openAccount(czlowiek)
czlowiek_konto.changeBalance(10)
print([konto.getId() for konto in konta])
kierwonik.openAccount(ludzik)
print([konto.getOwner().getFullName() for konto in konta])
for konto in konta:
    konto.changeBalance(-101)
print([konto.getBalance() for konto in konta])