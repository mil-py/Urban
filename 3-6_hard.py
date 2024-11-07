data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def dive(data):
    s = 0
    if type(data) == str:
        return len(data)
    elif type(data) == int or type(data) == float:
        return data
    elif type(data) == dict:
        for value, key in data.items():
            s += dive(value) + dive(key)
    else:
        for subdata in data:
            s += dive(subdata)
    return s


print(dive(data_structure))
