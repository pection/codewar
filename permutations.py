import itertools
def permutations(string):
    list_test = []
    for i in string:
        list_test.append(i)
    print(list_test)
    perm = itertools.permutations(list_test)
    perm = sorted(set(perm))
    saveres=""
    res = []
    for i in perm:
        for j in i:
            saveres+=j
        res.append(saveres)
        saveres=""
    return res
