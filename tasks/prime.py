__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    if number > 1:
        for i in range(2, number // 2 + 1):
            if (number % i) == 0:
                return False
        return True
    else:
        return False
