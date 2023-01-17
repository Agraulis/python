import timeit
import cProfile
import atkin as at
import eratosfen as er

NUMBERS = 500
LENGTH = 10

print(timeit.timeit('er.erat(10_000)', globals=globals(), number=1_000)) """3.484648872999969"""
print(timeit.timeit('at.sieveOfAtkin(10_000)', globals=globals(), number=1_000)) """18.249673336000342"""
"""
with open('task_2.txt', 'w') as res:
    for num in range(NUMBERS):
        res.write('#'.join(['erat', str(num), str(timeit.timeit('er.erat(LENGTH)', globals=globals(), number=num)), '\n']))
    for num in range(NUMBERS):
        res.write('#'.join(['atkin', str(num), str(timeit.timeit('at.sieveOfAtkin(LENGTH)', globals=globals(), number=num)), '\n']))
"""