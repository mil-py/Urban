def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        prime_flag = True
        for i in range(2, res // 2 + 1):
            if res % i == 0:
                prime_flag = False
                break

        print('Простое' if prime_flag else 'Составное')
        return res

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


print(sum_three(2, 3, 5))
