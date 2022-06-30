def canJump(nums):
    if len(nums) == 1:
            return True

    minStepsRequired = 0
    previousGood = len(nums)-1

    # work backwards and see if can reach final cell
    for i in range(len(nums)-2, -1, -1):
        minStepsRequired = previousGood - i
        if nums[i] >= minStepsRequired:
            previousGood = i

    return previousGood == 0

print(canJump([ 2, 3, 1, 1, 4 ]))
print(canJump([ 3, 2, 1, 0, 4 ]))
