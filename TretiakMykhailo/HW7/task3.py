def nums_of_characters(word: str, count_spaces = False) -> dict | None:
    """
    Returns the number of each character in the.

        Parameters:
                word (srt): A string, word in which you need to count characters.
                count_spaces (bool): A bool parameter, indicates whether to count spaces.

        Returns:
                num_characters (dict): numbers of characters.
                
    Returns None on error or a wrong data type.
    """
    
    try:
        # Check right types of args, 
        # give an exception and return None if wrong
        if type(word) is not str or type(count_spaces) is not bool:
            print(f"[!] Wrong data type(s). word: {type(word)}, count_spaces: {type(count_spaces)}")
            print(f"[!] Must be word: (str), count_spaces: (bool)")
            return None

        if not count_spaces:
            word = word.replace(' ', '')
            

        # Make dict like: {'h':1, 'e':1, 'l':2, 'o':1} from 'hello'
        num_characters = {x:word.count(x) for x in word}
        
        return num_characters
        
    except Exception as error:
        print(f"[!] Error: {error}")
        return None
    
    
def main():
    words = ['hello', 'Bye!', 'Good Morning!', 'I love Python', 'SoftServe']
    for word in words:
        print(f"Result of (word={word}, count_spaces=False): {nums_of_characters(word, False)}")
        print(f"Result of (word={word}, count_spaces=True): {nums_of_characters(word, True)}")
    
    print(f"Result of (word=123, count_spaces=True): {nums_of_characters(123, True)}")
    print(f"Result of (word=123, count_spaces=321): {nums_of_characters(123, 321)}")



if __name__ == '__main__':
    main()
  