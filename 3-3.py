def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print('\n', "1")
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

print('\n', "2")
values_list = ['uh', False, 12]
values_dict = {'a': 'oh', 'b': True, 'c': 21}

print_params(*values_list)

print_params(**values_dict)

print('\n', "3")
values_list_2 = ['uh', False]
print_params(*values_list_2, 42)
