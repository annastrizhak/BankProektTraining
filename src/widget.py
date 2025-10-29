import re
from datetime import datetime
from masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """
    Получает строку с типом и номером карты или счета и возвращает замаскированные данные.

    Аргумент data: строка вида "Visa Platinum 7000792289606361" или "Счет 73654108430135874305".
    Возвращает строку с замаскированными номерами.
    """

    # Регулярное выражение для разделения строки на два компонента: префикс и номер
    match = re.search(r"^(\D+)\s+(\d+)$", data.strip())
    if not match:
        raise ValueError("Неверный формат входных данных")

    # Префикс (название карты или счёт) и само число
    prefix, number = match.groups()

    # Определяем тип карточки или счёта
    known_cards = {'maestro', 'mastercard', 'visa'}
    if any(card in prefix.lower() for card in known_cards):
        # Применяем маску для номеров карт
        masked_number = get_mask_card_number(number)
    elif prefix.lower().startswith('счет'):
        # Применяем маску для номеров счетов
        masked_number = get_mask_account(number)
    else:
        raise ValueError(f"Недопустимый тип платежа '{prefix}'")

    # Формируем итоговую строку с сохранением исходного префикса
    return f"{prefix} {masked_number}"


def get_date(iso_string: str) -> str:
    """
    Преобразует дату из формата ISO 8601 в формат ДД.ММ.ГГГГ.

    :param iso_string: Дата в формате ISO 8601, например "2024-03-11T02:26:18.671407"
    :return: Дата в формате "11.03.2024"
    """

    try:
        dt = datetime.fromisoformat(iso_string)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Некорректный формат даты")
