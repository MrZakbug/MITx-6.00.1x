def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''

    result = 0
    for i in range(len(listA)):
        result += listA[i] * listB[i]
    return result

print(dotProduct([-58, -73, 96, -10, -53, -29, -95, 40, -96], [-51, -17, -29, -31, 80, 65, -8, -49, -94]))