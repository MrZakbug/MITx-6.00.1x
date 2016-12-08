def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    longest = []
    for i in range(len(L)):
        tempListDecreasing = []
        tempListDecreasing.append(L[i])
        tempListIncreasing = []
        tempListIncreasing.append(L[i])
        sameNumbers = []
        sameNumbers.append(L[i])
        for j in range(len(L)):
            if j >= i:
                if L[j] >= L[j - 1] and j != 0:
                    tempListIncreasing.append(L[j])
                    tempListDecreasing = []
                    tempListDecreasing.append(L[j])
                    if len(tempListIncreasing) > len(longest):
                        longest = tempListIncreasing.copy()

                if L[j] <= L[j - 1] and j != 0:
                    tempListDecreasing.append(L[j])
                    tempListIncreasing = []
                    tempListIncreasing.append(L[j])
                    if len(tempListDecreasing) > len(longest):
                        longest = tempListDecreasing.copy()
                if L[j] == L[j - 1] and j != 0:
                    sameNumbers.append(L[j])
                    if len(sameNumbers) > len(longest):
                        longest = sameNumbers.copy()

        if len(tempListIncreasing) > len(longest):
            longest = tempListIncreasing.copy()
        if len(tempListDecreasing) > len(longest):
            longest = tempListDecreasing.copy()

    return sum(longest)


print(longest_run([3, 4, 5, 6, 10, 20, 100, 200, 1, 3, 3, 3, -10, 1, 2, 3, 4]))