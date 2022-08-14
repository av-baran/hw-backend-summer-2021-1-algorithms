__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.6667
    """
    sum_even = 0
    sum_odd = 0

    for element in arr:
        if element % 2 == 0:
            sum_even = sum_even + element
        else:
            sum_odd = sum_odd + element

    try:
        result = sum_even / sum_odd
    except:
        result = 0

    result = round(result, 4)
    return result
