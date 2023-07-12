def findPrimeFactors(num):
    arr = []

    for i in range(2, num):
        if (num % i) == 0:
            isPrime = True

            for j in range(2, i):
                if i % j == 0:
                    isPrime = False
            if isPrime:
                arr.append(i)
    print(arr)
    return len(arr)


print(findPrimeFactors(5))
