from datetime import datetime
from masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """
    Получает строку с типом и номером карты или счета и возвращает замаскированные данные.
    Аргумент data: строка вида "Visa Platinum 7000792289606361" или "Счет 73654108430135874305".
    Возвращает строку с замаскированными номерами.
    """

    # Разделение строки на две части (первая — название карты или счет, вторая — номер)
    parts = data.strip().split(maxsplit=1)
    if len(parts) != 2:
        raise ValueError("Неверный формат входных данных")

    # Префикс (название карты или счет) и само число
    prefix, number = parts
    prefix_lower = prefix.lower()

    # Проверка известного типа карты или счета
    known_cards = ['maestro', 'mastercard', 'visa']
    if any(card in prefix_lower for card in known_cards):
        return get_mask_card_number(number)
    elif prefix_lower.startswith('счет'):
        return get_mask_account(number)
    else:
        raise ValueError(f"Недопустимый тип платежа '{prefix}'")


def get_date(iso_string: str) -> str:
    """
    Преобразует дату из формата ISO 8601 в формат ДД.ММ.ГГГГ.

    :param iso_string: Дата в формате ISO 8601, например "2024-03-11T02:26:18.671407"
    :return: Дата в формате "11.03.2024"
    """

    dt = datetime.fromisoformat(iso_string)
    return dt.strftime("%d.%m.%Y")
