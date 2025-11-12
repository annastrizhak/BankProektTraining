"""
Модуль масок для обработки банковских данных.
"""


def get_mask_card_number(card_number: str) -> str:
    """Получение маски банковской карты.
    Принимает на вход только 16-значный номер карты."""

    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Некорректный формат номера карты.")

    return f"{card_number[:4]} {card_number[4:6]}******{card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Получение маски банковского счёта."""

    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Некорректный формат номера счёта.")
    return f"**{account_number[-4:]}"
