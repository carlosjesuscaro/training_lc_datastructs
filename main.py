from recursivity import recursive_main
from palindrome import palindrome_main
from two_sum import two_sum_main
from two_array_sorted import combine

if __name__ == '__main__':
    print('Recursive exercise:')
    recursive_main()
    print('\nPalindrome exercise')
    palindrome_main()
    print('\nTwo sum exercise')
    two_sum_main()
    print('\nTwo array sum exercise')
    print(combine([1, 2, 3, 150, 450], [100, 200, 300, 302, 500]))

