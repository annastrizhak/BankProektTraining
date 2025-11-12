import pytest

from src.widget import get_date, mask_account_card


class TestWidget:
    @pytest.mark.parametrize(
        "data_string, expected_masked_string",
        [
            ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79******6361"),
            ("Maestro 1234567812345678", "Maestro 1234 56******5678"),
            ("Счет 73654108430135874305", "Счет **4305"),
            ("Счет 12345", "Счет **2345"),
            ("MasterCard 1111222233334444", "MasterCard 1111 22******4444"),
        ],
    )
    def test_mask_account_card_valid(self, data_string: str, expected_masked_string: str) -> None:
        """Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки."""
        assert mask_account_card(data_string) == expected_masked_string

    @pytest.mark.parametrize(
        "invalid_data_string, error_message_part",
        [
            ("Invalid format string", "Неверный формат входных данных"),
            ("Visa 123", "Некорректный формат номера карты"),
            ("Счет 123", "Некорректный формат номера счёта"),
            ("Unknown Type 1234567890123456", "Недопустимый тип платежа 'Unknown Type'"),
            ("", "Неверный формат входных данных"),
            ("   ", "Неверный формат входных данных"),
        ],
    )
    def test_mask_account_card_invalid(self, invalid_data_string: str, error_message_part: str) -> None:
        """Тестирование функции на обработку некорректных входных данных."""
        with pytest.raises(ValueError, match=error_message_part):
            mask_account_card(invalid_data_string)

    @pytest.mark.parametrize(
        "iso_string, expected_date",
        [
            ("2024-03-11T02:26:18.671407", "11.03.2024"),
            ("2023-12-01T23:59:59.000000", "01.12.2023"),
            ("1999-07-25T15:00:00", "25.07.1999"),
        ],
    )
    def test_get_date_valid(self, iso_string: str, expected_date: str) -> None:
        """Тестирование правильности преобразования даты."""
        assert get_date(iso_string) == expected_date

    @pytest.mark.parametrize(
        "invalid_iso_string",
        [
            "2024-13-11T02:26:18.671407",
            "2024-03-32T02:26:18.671407",
            "invalid-date-string",
            "",
            "   ",
        ],
    )
    def test_get_date_invalid(self, invalid_iso_string: str) -> None:
        """Проверка работы функции на некорректных входных форматах даты."""
        with pytest.raises(ValueError, match="Некорректный формат даты"):
            get_date(invalid_iso_string)
