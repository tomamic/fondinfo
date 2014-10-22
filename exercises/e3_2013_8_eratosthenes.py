import time

def primes1(n: int):
    nums = list(range(2, n + 1))
    j = 0
    while j < len(nums):
        x = nums[j]
        for i in range(x, n // x + 1):
            try:  # if x * i in nums
                nums.remove(x * i)
            except:
                pass
        j += 1
    return nums

def primes2(n: int):
    nums = []
    is_prime = [True] * (n + 1)
    for x in range(2, n + 1):
        if is_prime[x]:
            nums.append(x)
            for i in range(x, n // x + 1):
                is_prime[x * i] = False
    return nums

if __name__ == '__main__':
    n = int(input('n? '))
    t0 = time.clock()
    res1 = primes1(n)
    t1 = time.clock()
    res2 = primes2(n)
    t2 = time.clock()
    print(res1)
    print('A.', len(res1), 'primes found in', t1 - t0, 'seconds')
    print('B.', len(res2), 'primes found in', t2 - t1, 'seconds')
