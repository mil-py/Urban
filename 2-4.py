# рассортировать заданный массив целых чисел на простые и не простые
numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes=[]
not_primes = []

for i in range(0,len(numbers)):
    if numbers[i] ==1:
        continue
    isPrime = True
    for j in range(2,numbers[i]-1):
        if numbers[i] % j == 0:
            not_primes.append(numbers[i])
            isPrime = False
            break
    if isPrime:
        primes.append(numbers[i])
print('Primes: ', primes)
print('Not primes: ', not_primes)
