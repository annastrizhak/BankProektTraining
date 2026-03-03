from typing import List, Dict, Any
import pytest
from generators import filter_by_currency, transaction_descriptions, card_number_generator


# Фикстура с примером транзакций
@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}, "description": "Description1"},
        {"id": 2, "operationAmount": {"currency": {"code": "EUR"}}, "description": "Description2"},
        {"id": 3, "operationAmount": {"currency": {"code": "USD"}}, "description": "Description3"}
    ]


# Тестируем фильтр по валюте с разными значениями валюты
@pytest.mark.parametrize(
    "currency_code,expected_ids",
    [
        ("USD", [1, 3]),
        ("EUR", [2]),
        ("GBP", []),  # Валюта отсутствует среди примеров
    ],
)
def test_filter_by_currency(sample_transactions: List[Dict[str, Any]], currency_code: str, expected_ids: List[int]) -> None:
    filtered = list(filter_by_currency(sample_transactions, currency_code))
    actual_ids = [transaction["id"] for transaction in filtered]
    assert sorted(actual_ids) == sorted(expected_ids)


# Проверяем генератор описаний транзакций с пустым списком и заполненным
@pytest.mark.parametrize(
    "transactions,expected_descriptions",
    [
        ([], []),
        (
            [
                {"description": "Description1"},
                {"description": "Description2"},
                {"description": "Description3"},
            ],
            ["Description1", "Description2", "Description3"],
        ),
    ],
)
def test_transaction_descriptions(transactions: List[Dict[str, Any]], expected_descriptions: List[str]) -> None:
    desc_gen = transaction_descriptions(transactions)
    result_descriptions = list(desc_gen)
    assert result_descriptions == expected_descriptions


# Параметры для генератора карточных номеров
@pytest.mark.parametrize(
    "start,end,expected_cards",
    [
        (1, 5, ['0000 0000 0000 0001', '0000 0000 0000 0002', '0000 0000 0000 0003', '0000 0000 0000 0004', '0000 0000 0000 0005']),
        (1_000_000, 1_000_004, ['0000 0000 0100 0000', '0000 0000 0100 0001', '0000 0000 0100 0002', '0000 0000 0100 0003', '0000 0000 0100 0004'])
    ],
)
def test_card_number_generator(start: int, end: int, expected_cards: List[str]) -> None:
    generated_cards = list(card_number_generator(start, end))
    assert generated_cards == expected_cards
