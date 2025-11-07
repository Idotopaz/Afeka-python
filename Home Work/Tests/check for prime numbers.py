x = int(input("give me a number: "))
primes = []

for num in range(2, x + 1):
    for i in range(2, num):
        if num % i == 0:
                break
    else:
        primes.append(num)


print(x,primes)