# bank
Introduction project on OOP in Python

# Classes description:
- Account - an account that can be created in a bank. At initialization, it takes the currency, owner (which is an instance of class Person) and an ID, which is generated automatically while opening an account. It stores the owner as an instance of class Person, ID, current balance, max. debit, an array of operations and the currency.

- Bank - a class which stores accounts that has been opened in this bank and IDs of people that has their account open in this bank. It also stores the capital which is the sum of every accounts' balance.

- Banker - it extends the class Person. Banker can open and close accounts in the bank that they are hired.

- Boss - it extends the class Person, it takes one extra parameter - an instance of class Bank where they will be the boss. They can hire and fire bankers.

- Operation - it stores the operation type ('incoming transfer', 'withdraw', 'deposit' etc.), amount, an instance of class Person (sender or recipient), title and date.

- Person - it stores the name and surname of a person, an array of accounts that this person has opened and the default currency that this person works with.