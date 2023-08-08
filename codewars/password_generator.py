import string
import random

n=2
k=3
m=10

letters= random.sample(string.ascii_letters, m)
digits = random.sample(string.digits, k)
symbs = random.sample(list('!@%^&*()?/'), n)

predpass =letters+digits+symbs
random.shuffle(predpass)
password = ''.join(predpass)
print(password)
