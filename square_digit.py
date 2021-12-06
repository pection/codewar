def square_digits(num):
    res = [int(x) for x in str(num)]
    result = []
    for i in res:
        i = int(i)*int(i)
        result.append(i)
    return int(''.join(map(str,result)))
