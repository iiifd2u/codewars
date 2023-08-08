def valid_ISBN10(isbn):
    valid_field = '0123456789X'
    if len(isbn)!=10 or [el for el in isbn[:-1] if el not in valid_field[:-1]] or isbn[-1] not in valid_field:
        return False
    isbn_dict = {(idx+1):k.replace('X', '10') for idx, k in enumerate(list(isbn))}
    return sum(list(map(lambda x, y:x*y, isbn_dict.keys(), [int(el) for el in isbn_dict.values()])))%11==0

print(valid_ISBN10('048665088X'))

a =list(range(3,103))
import random
m=random.randint(3, 102)
m=3
print(f'm = {m}')
l =m-a[0]+1

print(f'количество чисел = {m}')
print()

natural = [1, 2]+a[:l]
print(*natural)
#m=3
kmin =3*2*1
# m=102
kmax = 102*101*100
print(f'kmax = {kmax}')

def f(x):
    return x*(x-1)*(x-2)

xs =[x for x in range(3, 103)]
ks = [f(x) for x in xs]
avg = sum(ks)/len(ks)
print(xs)
print(ks)
print('k_avg =', avg)
from fractions import Fraction
print('100/k= ', 100/avg)
print('100/k= ',Fraction(200, int(avg*2)))
print(Fraction(3, 9))