def is_prime(num):
    sqrt = int(num ** 0.5) + 1
    if num % 2 == 0:
        return False
    for i in range(3, sqrt, 2):
        if num % i == 0:
            return False
    return True


def run(num):
    # 600851475143
    nmax = int(num ** 0.5) + 1
    while num % 2 == 0:
        num //= 2
    if num == 1:
        print(2)
        return
    for i in range(3, nmax, 2):
        if num % i == 0 and is_prime(i):
            while num % i == 0 and num != i:
                num //= i
    print(num)


t = int(input().strip())
for counter in range(t):
    n = int(input().strip())
    run(n)
