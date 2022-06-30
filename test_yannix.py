def question_1(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return question_1(n-1) + question_1(n-2)
def question_2(s):
    if len(s) % 2 != 0:
        return False
    bracket = {'(' : ')', '[' : ']', '{' : '}'}
    stack = []
    for i in s:
        if i in bracket.keys():
            stack.append(i)
        else:
            if stack == []:
                return False
            a = stack.pop()
            if i!= bracket[a]:
                return False
    return stack == []

def question_3(nums):
    if len(nums) == 1:
            return True
    minStepsRequired = 0
    previousGood = len(nums)-1
    for i in range(len(nums)-2, -1, -1):
        minStepsRequired = previousGood - i
        if nums[i] >= minStepsRequired:
            previousGood = i
    return previousGood == 0
