# only check till squared root of num, deduce the rest

import os
import time

print("Running", os.path.basename(__file__))

prime_list = []


def is_prime(num):
    sqrt = int(num ** 0.5)
    for i in range(2, sqrt):
        if num % i == 0:
            return False
    return True


def run():
    num = 600851475143
    sqrt = int(num ** 0.5)
    for i in range(2, sqrt):
        if num % i == 0 and i not in prime_list and is_prime(i):
            prime_list.append(i)
    print(max(prime_list))
    return


start_time = time.time()
run()
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
