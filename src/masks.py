"""
Модуль масок для обработки банковских данных.
"""


def get_mask_card_number(card_number: int) -> str:
    """Получение маски банковской карты."""
    card_str = str(card_number)
    if len(card_str) != 16 or not card_str.isdigit():
        raise ValueError("Некорректный формат номера карты.")
    first_part = card_str[:6]
    last_part = card_str[-4:]
    masked_middle = "** **"
    return f"{first_part[:4]} {first_part[4:]} {masked_middle} {last_part}"


def get_mask_account(account_number: int) -> str:
    """Получение маски банковского счёта."""
    acc_str = str(account_number)
    if len(acc_str) < 4 or not acc_str.isdigit():
        raise ValueError("Некорректный формат номера счёта.")
    return f"**{acc_str[-4:]}"
