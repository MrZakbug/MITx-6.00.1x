"""
A function called dict_interdiff that takes in two dictionaries (d1 and d2). The function will return a tuple of two
dictionaries: a dictionary of the intersect of d1 and d2 and a dictionary of the difference of d1 and d2
"""

def dict_interdiff(d1, d2):
    result = ()
    temp_dict = {}
    if True:
        for key in d1:
            if key in d2:
                temp_dict[key] = d1[key] + d2[key]
        for key in d2:
            if key in d1:
                temp_dict[key] = d1[key] + d2[key]
        result += (temp_dict,)


        temp_dict = {}

        for key in d1:
            if key not in d2:
                temp_dict[key] = d1[key]
        for key in d2:
            if key not in d1:
                temp_dict[key] = d2[key]
        result += (temp_dict,)

    if False:
        for key in d1:
            if key in d2:
                temp_dict[key] = 'False'
        for key in d2:
            if key in d1:
                temp_dict[key] = 'False'
        result += (temp_dict, {})

    return result


print(dict_interdiff({1: 1, 2: 2, 3: 3}, {1: 1, 2: 2, 3: 3}))