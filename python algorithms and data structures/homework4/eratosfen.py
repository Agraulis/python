import cProfile


def erat(n):
    """
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.007    0.007 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 eratosfen.py:17(<listcomp>)
        1    0.006    0.006    0.007    0.007 eratosfen.py:4(erat)
        1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    """
    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1
    return [x for x in a if x]


if __name__ == '__main__':
    cProfile.run('erat(10_000)')
    print(erat(100))
