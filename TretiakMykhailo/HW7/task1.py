import random

def largest_num(number1: int, number2: int) -> int:
    """
    Returns the largest of two decimal numbers.

        Parameters:
                number1 (int): A decimal integer
                number2 (int): Another decimal integer

        Returns:
                largest_number (int): Largest decimal number of number1 and number2
    """
    
    try:
        DATA_TYPES = (int, float)
        # Check right types of args, 
        # give an exception and return Zero if wrong
        if type(number1) not in DATA_TYPES or type(number2) not in DATA_TYPES:
            print(f"[!] Wrong data type(s). number1: {type(number1)}, number2: {type(number2)}")
            print(f"[!] Both types must be integers (int) or float (float)")
            return 0
        
        largest_number = max([int(number1), int(number2)]) # max() give us largest number
        return largest_number # return result (largest_num)
    except Exception as error:
        print(f"[!] Error: {error}")
        return 0
    

def main():
    print(f"Result of (1, 2): {largest_num(1, 2)}")
    print(f"Result of (6, 6): {largest_num(6, 6)}")
    print(f"Result of (100, 10): {largest_num(100, 10)}")
    print(f"Result of ('abc', 10): {largest_num('abc', 10)}")
    
    # Show results of 10 tries with random numbers
    for i in range(10):
        num1 = random.randrange(1, 200)
        num2 = random.randrange(1, 200)
        print(f"Result of ({num1}, {num2}): {largest_num(number1=num1, number2=num2)}")
        
    
    # Test cases
    assert largest_num(1, 2) == 2
    assert largest_num(2, 1) == 2
    assert largest_num(5, 5) == 5
    assert largest_num(10, 11) == 11
    assert largest_num(100, 10) == 100
    
        

if __name__ == '__main__':
    main()
  