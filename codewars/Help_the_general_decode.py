import string
alfa = string.ascii_letters
alfa_digits = (string.ascii_letters+string.digits+'., ?/')
alfa_symbs = list(string.punctuation)
alfa_symbs.remove('.')
alfa_symbs.remove(',')
alfa_symbs.remove('?')




print('alphabet = {} '.format(alfa_digits))
print('len(alfa) = {}'.format(len(alfa_digits)))
#print(alfa[1::2])
#print(alfa[3::4])
#print(alfa[7::8])


di ={el:idx for idx, el in enumerate(alfa_digits)}
print(di)
def encode(word):
    own_alpha = alfa_digits
    coded = ''

    for idx, letter in enumerate(list(word)):
        if letter in alfa_symbs:
            coded+=letter
        else:
            new_st = (2**(idx+1)*(di[letter]+1)-1)%67
            #print('delimer ={}'.format((2**(idx+1)*(di[letter]+1)-1)//67))
            coded += own_alpha[new_st]
    return coded



print(encode('aaaaaaaaaa'))
print(encode('bbbbbbbb'))
# print(encode('Hello World!'))


a, b, c ='', '', ''
for w in string.ascii_lowercase[:10]:
    a+=encode(''+w)[0]
    b += encode('_' + w)[1]
    c += encode('__' + w)[2]

print('a = {}'.format(a))
print('b = {}'.format(b))
print('c = {}'.format(c))



def decode(code):
    di = {el: idx for idx, el in enumerate(alfa_digits)}
    decoded=''
    dec_dict = {v:k for k, v in di.items()}
    for idx, l in enumerate(code):
        if l in alfa_symbs:
            decoded+=l
        else:
            st = 2 ** (idx + 1)
            dec_cand = (di[l]+1)/(st)-1
            for dc in range(len(dec_dict)):
                if (st*(dc+1) - di[l]-1)%67 == 0:
                    dec_cand = dc
            decoded += dec_dict[int(dec_cand)]
    return decoded


print(encode('Hello World!'))
print(decode(encode('Hello World!Hello World!')))
print(decode(encode('a'*len(list('atC5kfOuKAr!')))))
