import random

li = list(range(1, 65))
xs = random.sample(li, 32)
ys = list(set(li)-set(xs))
winners_I = [min(x, y) for x, y in zip(xs, ys)]
# print(xs)
# print(ys)
# print('winners_I = ', winners_I)

n=64
winners = list(range(1, 65))
counter=0
from fractions import Fraction
for _ in range(100):
    n = 64
    winners = list(range(1, 65))
    for i in range(6):
        n=n//2
        xs = random.sample(winners, n)
        ys = list(set(li) - set(xs))
        winners = [min(x, y) for x, y in zip(xs, ys)]
        if i==4 and 2 in winners:
            counter+=1
        #print('winners({}) = {}'.format(i+1, winners))
print(counter/100)
print(Fraction(counter/100))
print(62/63)
a = (1/63+1/31+1/15+1/7+1/3+1)
print(Fraction(a))
a=155+63*5+3*3*31*5+3*7*31*5
b=3*7*3*31*5
print(a+b)
print(b*6)
print()
