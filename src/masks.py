"""
Модуль масок для обработки банковских данных.
"""


def get_mask_card_number(card_number: str) -> str:
    """Получение маски банковской карты."""

    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Некорректный формат номера карты.")
    first_part = card_number[:6]
    last_part = card_number[-4:]
    masked_middle = "** ****"
    return f"{first_part[:4]} {first_part[4:6]}{masked_middle} {last_part}"


def get_mask_account(account_number: str) -> str:
    """Получение маски банковского счёта."""

    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Некорректный формат номера счёта.")
    return f"**{account_number[-4:]}"
