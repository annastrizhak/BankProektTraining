import pytest
from datetime import datetime
from typing import Any, Dict, List


@pytest.fixture
def sample_operations() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-15T10:00:00.000000", "amount": 100},
        {"id": 2, "state": "PENDING", "date": "2023-01-12T10:00:00.000000", "amount": 50},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-14T10:00:00.000000", "amount": 200},
        {"id": 4, "state": "CANCELED", "date": "2023-01-01T10:00:00.000000", "amount": 10},
        {"id": 5, "state": "EXECUTED", "date": "2023-01-15T10:00:01.000000", "amount": 120},
        {"id": 6, "state": "EXECUTED", "date": "2023-01-20T10:00:00.000000", "amount": 300},
        {"id": 7, "state": "PENDING", "date": "2023-01-05T10:00:00.000000", "amount": 75},
    ]


@pytest.fixture
def empty_operations() -> List[Any]:
    return []


@pytest.fixture
def operations_with_missing_state() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "date": "2023-01-10T10:00:00.000000", "amount": 100},
        {"id": 2, "state": "EXECUTED", "date": "2023-01-11T10:00:00.000000", "amount": 50},
    ]


@pytest.fixture
def dt_objects() -> Dict[str, datetime]:
    return {
        "2023-01-15T10:00:00.000000": datetime.fromisoformat("2023-01-15T10:00:00.000000"),
        "2023-01-10T11:00:00.000000": datetime.fromisoformat("2023-01-10T11:00:00.000000"),
    }
