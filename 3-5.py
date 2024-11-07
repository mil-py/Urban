def get_multiplied_digits(n):
    str_n = str(n)
    first = int(str_n[0])
    if len(str_n) == 1:
        return first

    return first * get_multiplied_digits(int(str_n[1:]))


print(get_multiplied_digits(40203))
