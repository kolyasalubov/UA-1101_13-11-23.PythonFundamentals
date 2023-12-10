def check_numbers(start, end):
    # Even numbers that are divisible by 2
    even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]

    # Odd numbers that are divisible by 3
    odd_numbers_divisible_by_3 = [num for num in range(start, end + 1) if num % 2 != 0 and num % 3 == 0]

    # Numbers that are not divisible by 2 and 3
    not_divisible_by_2_and_3 = [num for num in range(start, end + 1) if num % 2 != 0 and num % 3 != 0]

    # Return the results
    return {
        "even_numbers": even_numbers,
        "odd_numbers_divisible_by_3": odd_numbers_divisible_by_3,
        "not_divisible_by_2_and_3": not_divisible_by_2_and_3
    }

result = check_numbers(1, 10)

print("Even numbers that are divisible by 2:", result["even_numbers"])
print("Odd numbers that are divisible by 3:", result["odd_numbers_divisible_by_3"])
print("Numbers that are not divisible by 2 and 3:", result["not_divisible_by_2_and_3"])
