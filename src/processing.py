
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
