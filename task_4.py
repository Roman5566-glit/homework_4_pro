class InsufficientResourcesException(Exception):
    """Исключение при нехватке ресурсов"""

    def __init__(self, required_resource, required_amount, current_amount):
        self.required_resource = required_resource
        self.required_amount = required_amount
        self.current_amount = current_amount
        super().__init__(f"Недостаточно ресурса: {required_resource}")


def cast_spell(player_mana):
    required = 50

    if player_mana < required:
        raise InsufficientResourcesException("мана", required, player_mana)

    print("Заклинание применено")


try:

    cast_spell(20)

except InsufficientResourcesException as exc:

    print("Ошибка:", exc.required_resource)
    print("Нужно:", exc.required_amount)
    print("Есть:", exc.current_amount)
