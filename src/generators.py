from typing import List, Dict, Iterator, Any


def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """
    Функция-фильтр, которая возвращает итератор транзакций,
    соответствующие заданной валюте.

    :param transactions: список словарей-транзакций
    :param currency_code: код валюты (например, 'USD')
    :yield: транзакции с нужной валютой
    """
    for t in transactions:
        op_amount = t.get("operationAmount", {})  # Точно знаем, что это словарь
        currency = op_amount.get("currency", {})
        code = currency.get("code")
        if isinstance(code, str) and code == currency_code:
            yield t


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генерирует итератор, выдающий описания всех транзакций.

    :param transactions: список словарей-транзакций
    :yield: описание каждой транзакции
    """
    for t in transactions:
        yield t.get("description", "")  # Ожидаем строку, возвращаем строку


def card_number_generator(start: int = 1, end: int = 9999999999999999) -> Iterator[str]:
    """
    Генерирует номера банковских карт в указанном диапазоне.

    :param start: начало диапазона номеров карт
    :param end: конец диапазона номеров карт
    :yield: карта в формате XXXX XXXX XXXX XXXX
    """
    fmt = "{:016d}".format
    for i in range(start, end + 1):
        formatted_num = fmt(i)
        yield f"{formatted_num[:4]} {formatted_num[4:8]} {formatted_num[8:12]} {formatted_num[12:]}"
