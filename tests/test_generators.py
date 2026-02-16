from typing import List, Dict, Any
import pytest
from generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}, "description": "Description1"},
        {"id": 2, "operationAmount": {"currency": {"code": "EUR"}}, "description": "Description2"},
        {"id": 3, "operationAmount": {"currency": {"code": "USD"}}, "description": "Description3"}
    ]


def test_filter_by_currency(sample_transactions: List[Dict[str, Any]]) -> None:
    usd_gen = filter_by_currency(sample_transactions, "USD")
    assert next(usd_gen)["id"] == 1
    assert next(usd_gen)["id"] == 3
    with pytest.raises(StopIteration):
        next(usd_gen)


def test_filter_by_unmatched_currency(sample_transactions: List[Dict[str, Any]]) -> None:
    eur_gen = filter_by_currency(sample_transactions, "JPY")
    with pytest.raises(StopIteration):
        next(eur_gen)


def test_empty_input() -> None:
    empty_gen = filter_by_currency([], "USD")
    with pytest.raises(StopIteration):
        next(empty_gen)


def test_transaction_descriptions(sample_transactions: List[Dict[str, Any]]) -> None:
    desc_gen = transaction_descriptions(sample_transactions)
    expected_descs = ["Description1", "Description2", "Description3"]
    for idx, desc in enumerate(desc_gen):
        assert desc == expected_descs[idx]


def test_empty_descriptions() -> None:
    gen = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(gen)


def test_card_number_generator() -> None:
    cards = list(card_number_generator(1, 5))
    assert cards == ['0000 0000 0000 0001',
                     '0000 0000 0000 0002',
                     '0000 0000 0000 0003',
                     '0000 0000 0000 0004',
                     '0000 0000 0000 0005']


def test_large_range() -> None:
    first_five = list(card_number_generator(1_000_000, 1_000_004))
    assert first_five == ['0000 0000 0100 0000',
                          '0000 0000 0100 0001',
                          '0000 0000 0100 0002',
                          '0000 0000 0100 0003',
                          '0000 0000 0100 0004'
                          ]
