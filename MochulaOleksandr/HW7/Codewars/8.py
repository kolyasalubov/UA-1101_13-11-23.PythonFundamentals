def zero_fuel(distance_to_pump, mpg, fuel_left):
    x = distance_to_pump / mpg
    if x <= fuel_left:
        return True
    else:
        return False