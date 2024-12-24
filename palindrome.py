def check_palindrome(str_input: str) -> bool:
    """
    Checks whether the input is a palindrome

    Args:
        str_input (str): the input string
    Returns:
        bool
    Raises:
        TypeError: if the input is not a string
    """
    try:
        i, j = 0, len(str_input)-1
        while i <= j:
            if str_input[i].lower() == str_input[j].lower():
                i+=1
                j-=1
            else:
                return False
        return True

    except TypeError:
        print("Input must be a string")
        return False

def palindrome_main():
    word = 'iamai'
    palindrome =check_palindrome(word)
    print(f'The word {word} is a palindrome: {palindrome}')
