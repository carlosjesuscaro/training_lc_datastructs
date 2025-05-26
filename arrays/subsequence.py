def subsequence(small: str, big: str) -> bool:
    status, i = False, 0
    while not status:
        for j in range(len(big)):
            if small[i] == big[j]:
                i+=1
                if i == len(small):
                    status = True
                    break
        break
    return status

def subsequence_main():
    print(f"Subsequent status: {subsequence('nalu', 'alianzanaluwaterloo')}")

