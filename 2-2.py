first = input("первое число = ")
second = input("второе число = ")
third = input("третье число = ")
print("равных чисел: ", end='')
if first == second and first == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)
