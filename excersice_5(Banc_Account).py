class BankAccount:
    def __init__(self, balance:int, interest_rate:float):
        self.__balance = balance
        self.__interest_rate = interest_rate
        self.__transactions = []

    def get_balance(self):
        """Метод для получения баланса"""
        return self.__balance

    def deposit(self, amount:int):
        """Метод для пополнения баланса."""
        self.__balance += amount
        self.__transactions.append(f"Внесение наличных на счёт: {amount}")

    def withdraw(self, amount:int):
        """Метод для снятия наличных с баланса."""
        if self.__balance - amount >= 0:
            self.__balance -= amount
            self.__transactions.append(f"Снятие наличных: {amount}")
        else:
            print(f"""Запрет на снятие {amount}. Недостаточно средста на счёте.""")
            self.__transactions.append(f"""Запрет на снятие {amount}. Недостаточно средста на счёте.""")

    def add_interset(self):
        """Метод добавляет проценты к счёту."""
        procenti = self.__balance * self.__interest_rate
        self.__balance += procenti
        self.__transactions.append(f"""Начислены проценты по вкладу: {procenti}""")

    def history(self):
        """Метод для вывода истории операций по счёту."""
        for i in self.__transactions:
            print(i)

#Проверка работы на экземпляре
if __name__ == '__main__':
    #Создаём экземпляр аккаунта пользователя.
    account = BankAccount(100000, 0.06)
    #Вносим 15000 на счёт.
    account.deposit(15000)
    #Снимаем 115000.
    account.withdraw(115000)
    #Проверяем что баланс нулевой.
    print(f"Баланс: {account.get_balance()}")
    #Пробуем снять ещё деньги и убеждаемся в запрете.
    account.withdraw(1000)
    #Проверяем что баланс не изменился.
    print(f"Баланс: {account.get_balance()}")
    #Внесём 1000 для проверки расчёта и зачисления процентов.
    account.deposit(1000)
    #Расчёт и зачисление процентов
    account.add_interset()
    #Проверка баланса
    print(f"Баланс: {account.get_balance()}")
    print('-'*20)
    #Выводи историю операций по счёту.
    account.history()