class InsufficientFundsException(Exception):
    """Исключение при нехватке денег"""

    def __init__(self, need, balance, currency="USD", transaction_type="withdrawal"):
        self.need = need
        self.balance = balance
        self.currency = currency
        self.transaction_type = transaction_type

        super().__init__("Недостаточно средств")


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsException(amount, balance, "USD", "withdrawal")

    balance -= amount
    print("Операция выполнена. Новый баланс:", balance)


try:

    withdraw(100, 200)

except InsufficientFundsException as exc:

    print("Ошибка:", exc)
    print("Нужно:", exc.need, exc.currency)
    print("Баланс:", exc.balance, exc.currency)
    print("Тип операции:", exc.transaction_type)
