import pytest
from masks import get_mask_card_number, get_mask_account


class TestMasks:
    @pytest.mark.parametrize(
        "card_number, expected",
        [
            ("1234567812345678", "1234 56******5678"),
            ("9876543210987654", "9876 54******7654"),
            ("0000000000000000", "0000 00******0000"),
        ],
    )
    def test_get_mask_card_number_valid(self, card_number: str, expected: str) -> None:
        """Тестирование правильности маскирования номера карты."""
        assert get_mask_card_number(card_number) == expected

    @pytest.mark.parametrize(
        "invalid_card_number",
        [
            "123",
            "123456781234567",
            "123456781234567A",
            "",
            "   ",
        ],
    )
    def test_get_mask_card_number_invalid(self, invalid_card_number: str) -> None:
        """Проверка работы функции на некорректных входных форматах номеров карт."""
        with pytest.raises(ValueError, match="Некорректный формат номера карты."):
            get_mask_card_number(invalid_card_number)

    @pytest.mark.parametrize(
        "account_number, expected",
        [
            ("12345678901234567890", "**7890"),
            ("00000000000000000000", "**0000"),
            ("1234", "**1234"),
        ],
    )
    def test_get_mask_account_valid(self, account_number: str, expected: str) -> None:
        """Тестирование правильности маскирования номера счета."""
        assert get_mask_account(account_number) == expected

    @pytest.mark.parametrize(
        "invalid_account_number",
        [
            "123",
            "abcde",
            "",
            "   ",
        ],
    )
    def test_get_mask_account_invalid(self, invalid_account_number: str) -> None:
        """Проверка работы функции с некорректными форматами и длинами номеров счетов."""
        with pytest.raises(ValueError, match="Некорректный формат номера счёта."):
            get_mask_account(invalid_account_number)
