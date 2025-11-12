import pytest
from processing import filter_by_state, sort_by_date
from typing import Any, Set


class TestProcessing:
    @pytest.mark.parametrize(
        "state_filter, expected_ids",
        [
            ("EXECUTED", {1, 3, 5, 6}),
            ("PENDING", {2, 7}),
            ("CANCELED", {4}),
            ("NON_EXISTENT", set()),
        ],
    )
    def test_filter_by_state(self, sample_operations: list[dict[str, Any]], state_filter: str, expected_ids: Set[int]) -> None:
        """Тестирование фильтрации списка словарей по заданному статусу."""
        filtered = filter_by_state(sample_operations, state_filter)
        actual_ids = {op["id"] for op in filtered}
        assert actual_ids == expected_ids

    def test_filter_by_state_default_executed(self, sample_operations: list[dict[str, Any]]) -> None:
        """Проверка работы функции с дефолтным значением 'EXECUTED'."""
        filtered = filter_by_state(sample_operations)
        actual_ids = {op["id"] for op in filtered}
        assert actual_ids == {1, 3, 5, 6}

    def test_filter_by_state_empty_list(self, empty_operations: list[Any]) -> None:
        """Проверка работы функции при пустом входном списке."""
        assert filter_by_state(empty_operations) == []

    def test_filter_by_state_missing_key(self, operations_with_missing_state: list[dict[str, Any]]) -> None:
        """Проверка обработки словарей без ключа 'state'."""
        filtered = filter_by_state(operations_with_missing_state, 'EXECUTED')
        actual_ids = {op["id"] for op in filtered}
        assert actual_ids == {2}

    @pytest.mark.parametrize(
        "descending, expected_order_ids",
        [
            (True,
             [6, 5, 1, 3, 2, 7, 4]),
            (False,
             [4, 7, 2, 3, 1, 5, 6]),
        ],
    )
    def test_sort_by_date(self, sample_operations: list[dict[str, Any]], descending: bool,
                          expected_order_ids: list[int]) -> None:
        """Тестирование сортировки списка словарей по датам."""
        sorted_data = sort_by_date(sample_operations, descending)
        actual_ids = [op["id"] for op in sorted_data]
        assert actual_ids == expected_order_ids

    def test_sort_by_date_empty_list(self, empty_operations: list[Any]) -> None:
        """Проверка сортировки пустого списка."""
        assert sort_by_date(empty_operations) == []

    def test_sort_by_date_invalid_date_format(self) -> None:
        """Тесты на работу функции с некорректными форматами дат."""
        data_with_bad_date: list[dict[str, Any]] = [
            {"id": 1, "state": "EXECUTED", "date": "2023-01-15", "amount": 100},
            {"id": 2, "state": "EXECUTED", "date": "invalid-date", "amount": 50},
        ]
        with pytest.raises(ValueError):
            sort_by_date(data_with_bad_date)

    def test_sort_by_date_missing_date_key(self) -> None:
        """Тест на отсутствие ключа 'date'."""
        data_missing_date: list[dict[str, Any]] = [
            {"id": 1, "state": "EXECUTED", "amount": 100},
        ]
        with pytest.raises(KeyError):
            sort_by_date(data_missing_date)
