def efficient(nums: list[int])->list[int]:
    new_nums = [0] * len(nums)
    i, j, z = 0, len(nums) - 1, len(nums) - 1
    while i <= j:
        if abs(nums[i]) >= abs(nums[j]):
            new_nums[z] = nums[i]**2
            i += 1
        else:
            new_nums[z] = nums[j] ** 2
            j -= 1
        z -= 1
    return new_nums

cc = efficient([-4,-1,0,3,10])
print(cc)

