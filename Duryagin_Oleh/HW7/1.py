from __future__ import annotations

from typing import Union


def largest(number1: int | float, number2: int | float) -> Union[str, int]:
    """
    The function takes two numbers and returns the largest of them
    """
    if not isinstance(number1 or number2, (int, float)):
        return "Wrong type"
    return max(number1, number2)


print(largest(2.666, 2.6666))
