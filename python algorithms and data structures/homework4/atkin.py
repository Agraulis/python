import math
import cProfile




def sieveOfAtkin(limit):
    """
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.027    0.027 <string>:1(<module>)
        1    0.026    0.026    0.027    0.027 atkin.py:7(sieveOfAtkin)
        1    0.000    0.000    0.027    0.027 {built-in method builtins.exec}
      102    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
     1227    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    """
    P = [2, 3]
    sieve = [False] * (limit + 1)
    for x in range(1, int(math.sqrt(limit)) + 1):
        for y in range(1, int(math.sqrt(limit)) + 1):
            n = 4 * x**2 + y**2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3 * x**2 + y**2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3 * x**2 - y**2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]
    for x in range(5, int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2, limit + 1, x**2):
                sieve[y] = False
    for p in range(5, limit):
        if sieve[p]:
            P.append(p)
    return P


if __name__ == '__main__':
    cProfile.run('sieveOfAtkin(10_000)')
    print(sieveOfAtkin(100))
