def subsequence(small: str, big: str) -> bool:
    status, i, j = False, 0, 0
    while j < len(big):
        if small[i] == big[j]:
            i += 1
            j += 1
        else:
            j += 1

        if i == len(small):
            status = True
            break
    return status

def subsequence_main():
    print(f"Subsequent status: {subsequence('nalu', 'alianzanaluwaterloo')}")



