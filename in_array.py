def in_array(array1, array2):
    res=[]
    for i in array1:
        for j in array2:
            if i in j and i not in res:
                res.append(i)
                break
    return sorted(res)
