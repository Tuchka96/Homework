nums = [0, 2, 4, 6, 8, 10]
i = 0
n = nums[i + 1] - nums[i]
while i < len(nums) - 1:
    n1 = nums[i + 1] - nums[i]
    if n1 != n:
        print("Нет")
        break
    elif i == len(nums) - 2:
        print("Да")
    i += 1
