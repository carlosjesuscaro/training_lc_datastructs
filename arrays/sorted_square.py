def sorted_squares(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2

    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums

# aa = sorted_squares([-100, -4, -1, 0, 3, 10, 101])
aa = sorted_squares([-4,-4,-3])
print(aa)

def new_sorted_sq(nums: list[int]) -> list[int]:
    j = -1
    check = True
    while check:
        flag = True
        if nums[0] < 0:
            nums[0] = -nums[0]
            while flag:
                if nums[0] <= nums[j]:
                    if j != -len(nums):
                        j -= 1
                    else:
                        break
                else:
                    nums.insert(j, nums[0])
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    nums.pop(0)
                    break
        else:
            break

    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    return nums


# bb = new_sorted_sq([-10, -9, -8, -5, -3, 0, 1, 2, 3, 4, 5, 9])
# bb = new_sorted_sq([-4, -4, -3])
bb = new_sorted_sq([-4,-1,0,3,10])
print(bb)

