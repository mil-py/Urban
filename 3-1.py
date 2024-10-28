
calls = 0

def count_calls():
    global calls
    calls+=1

def string_info(str):
    count_calls()
    return (len(str), str.upper(), str.lower())

def is_contains(str, lst):
    count_calls()
    contains = False
    for elem in lst:
        if elem.upper() == str.upper():
            contains = True
            break

    return contains

print(string_info('Krakozabra'))
print(string_info('Python ruliTT'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
