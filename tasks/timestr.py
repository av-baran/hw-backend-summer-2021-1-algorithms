from datetime import timedelta, datetime

__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    td = timedelta(seconds=seconds)
    d = datetime(1,1,1) + td
    days_str = f'{(d.day - 1):02d}d' if (d.day - 1) else ''
    hours_str = f'{d.hour:02d}h' if d.hour or days_str else ''
    minutes_str = f'{d.minute:02d}m' if d.minute or hours_str else ''
    seconds_str = f'{d.second:02d}s'

    result = "".join([days_str, hours_str, minutes_str, seconds_str])

    return result


