def move_zeros(array):
    list=[]
    while 0 in array:
        array.pop(array.index(0))
        list.append(0)
    array+=list
    return array
