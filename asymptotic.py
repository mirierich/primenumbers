def primes_method1(n):
    out = list()
    for num in range(1, n+1):
        prime = True
        for i in range(2, num):
            if (num % i == 0):
                prime = False
        if prime:
            out.append(num)
    return out


print("Test Case 6: ")
print(primes_method1(75))