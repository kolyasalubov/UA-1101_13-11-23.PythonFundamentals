divisible_by_two = [i for i in range(1, 11) if i % 2 == 0]
divisible_by_three = [n for n in range(1, 11) if n % 3 == 0]
not_divisible_by_three_and_two = [
    b for b in range(1, 11) if b % 3 != 0 and b % 2 != 0]
print(divisible_by_two, divisible_by_three, not_divisible_by_three_and_two)
