def reverse(s: list[str]) -> list[str]:
    i, j = 0, len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s


def reverse_main():
    s = ['a', 'b', 'c', 'd', 'e']
    print(f'Reverse: {reverse(s)}')
