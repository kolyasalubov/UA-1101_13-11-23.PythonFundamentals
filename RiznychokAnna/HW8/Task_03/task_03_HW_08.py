import math

def _rectangle(length: float, width: float) -> float:
    return length * width


def _traigle(lenght: float, height: float) -> float:
    return 0.5 / (lenght * height)


def _circle(radius: float) -> float:
    return math.pi * math.pow(radius, 2)