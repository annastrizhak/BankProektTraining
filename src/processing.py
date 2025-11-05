from datetime import datetime


def filter_by_state(data: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    Args:
        data (list[dict]): Список словарей для фильтрации.
        state (str, optional): Значение ключа 'state' для фильтрации.
                               По умолчанию 'EXECUTED'.

    Returns:
        list[dict]: Новый список словарей, где каждый словарь
                    имеет ключ 'state' со значением, равным переданному аргументу.
    """
    # Создаем новый список, содержащий только словари,
    # у которых значение ключа 'state' совпадает с аргументом.
    filtered_data = [item for item in data if item.get('state') == state]
    return filtered_data


def sort_by_date(data: list[dict], descending: bool = True) -> list[dict]:
    """
    Сортирует список словарей по дате, указанной в ключе 'date'.

    Args:
        data (list[dict]): Список словарей для сортировки.
                           Каждый словарь должен содержать ключ 'date' со значением в формате ISO 8601.
        descending (bool, optional): Порядок сортировки.
                                     True для сортировки по убыванию (новые первыми),
                                     False для сортировки по возрастанию (старые первыми).
                                     По умолчанию True.

    Returns:
        list[dict]: Новый список словарей, отсортированный по дате.
    """
    # Создаем новый список, чтобы не изменять оригинальные данные
    sorted_data = sorted(
        data,
        # Ключ для сортировки: преобразуем строку даты в объект datetime
        key=lambda x: datetime.fromisoformat(x['date'].replace('Z', '+00:00')),
        # Указываем порядок: reverse=True для убывания, reverse=False для возрастания
        reverse=descending
    )
    return sorted_data
