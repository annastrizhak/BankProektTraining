
from datetime import datetime


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


def mask_account_card(data: str) -> str:
    """
    Функция принимает строку с типом и номером карты/счета и возвращает замаскированное значение.

    :param data: Строка вида "Имя карточки 7000792289606361" или "Счет 73654108430135874305"
    :return: Замасированная строка
    """
    parts = data.rsplit(maxsplit=1)  # Разбиение строки на 2 части по последнему пробелу
    label, number = parts[0], parts[1]

    try:
        num_int = int(number)

        # Определяем, карта это или счёт по количеству цифр
        if len(str(num_int)) == 16:
            masked_num = get_mask_card_number(num_int)
        else:
            masked_num = get_mask_account(num_int)

        return f"{label} {masked_num}"
    except Exception as e:
        return f"Ошибка: {str(e)}"


def get_date(iso_string: str) -> str:
    """
    Преобразует дату из формата ISO 8601 в формат ДД.ММ.ГГГГ.

    :param iso_string: Дата в формате ISO 8601, например "2024-03-11T02:26:18.671407"
    :return: Дата в формате "11.03.2024"
    """
    dt = datetime.fromisoformat(iso_string)
    return dt.strftime("%d.%m.%Y")
