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

print(question_2("(["))
print(question_2("([)]"))
print(question_2("{[]}"))
