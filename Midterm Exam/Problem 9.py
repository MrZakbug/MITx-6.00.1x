def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    flatList = []
    for i in range(0, len(aList)):
        if type(aList[i]) is not list:
            flatList.append(aList[i])
        else:
            flatList.extend(flatten(aList[i]));
    return flatList

print(flatten([[1, [2, 3]], [[4, 5, 6], [7, [8, 9]]], [[3, 2, 1], [2, 1], [1, [0]]]]))