class BankAccount:
    def __init__(self, balance, interest_rate):
        self.__balance = balance
        self.__interest_rate = interest_rate
        self.__transactions = []

    def deposit(self, value):
        """Метод для пополнения баланса."""
        