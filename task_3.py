class GameEventException(Exception):
    """Исключение для игровых событий"""

    def __init__(self, event_type, details):
        self.event_type = event_type
        self.details = details
        super().__init__(f"Game event: {event_type}")


try:
    raise GameEventException(
        "death",
        {"reason": "удар мечом"}
    )

except GameEventException as exc:

    print("Игровое событие:", exc.event_type)
    print("Детали:", exc.details)
