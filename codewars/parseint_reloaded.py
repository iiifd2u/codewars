import re

def parse_int(number):
    number = re.sub(r'\sand\s', ' ', number)
    dict_vals = {'on':1, 'tw':2,
            'th':3, 'fo':4,
            'fi':5, 'si':6,
            'se':7, 'ei':8,
            'ni':9, 'te':10,
            'ze':0
            }
    dict_eltw = {'eleven':11, 'twelve':12}
    dict_mul={'hundred':100,
              'thousand':1000, 'million':1000000}
    #teen
    for k, v in dict_vals.items():
        number=re.sub(k+r'\w+teen', str(v+10), number)
    #ty
    tys = [sum([dict_vals[el[:2]]*10**(1-i)
                for i, el in enumerate(ty.split('-'))])
           for ty in re.findall(r'\w+ty-\w+', number)]
    for el in tys:
        number = re.sub(r'\w+ty-\w+', str(el),  number)
    for k, v  in dict_vals.items():
        number = re.sub(k+r'\w+ty', str(v*10)+' ',  number)
    #11_12
    for k, v in dict_eltw.items():
        number = re.sub(k, str(v), number)
    # nums
    for k, v in dict_vals.items():
        for _ in range(len(number.split())):

            if number.split()[-1][:2]!=k:
                number = re.sub(k + r'\w{0,5}\s+', str(v) + ' ', number)
            else:
                number = re.sub(k + r'\w{0,5}', str(v) + ' ', number)
    #10_100_1000

    a=number.split()
    if a[-1] in dict_mul.keys():
        a.append('0')
    number=' '.join(a)
    for k, v in dict_mul.items():
        arr = re.findall(r'\d+'+k+r'\d+', number.replace(' ', ''))
        for i in range(len(arr)):
            n = [int(el) for el in arr[i].split(k)]
            arr[i] = str(n[0]) + ' '+k+' ' + str(n[1])
            number = number.replace(arr[i], str(n[0] * v + n[1]), 1)
    return number



st = 'seven hundred eighty-three thousand nine hundred and nineteen'
print('783919:', parse_int(st))
st2 = 'eighty-three thousand nine hundred and nineteen'
print('83919:', parse_int(st2))
#print(parse_int('one'))
#print(parse_int(st))
#print(parse_int('one thousand twenty'))
print('101:', parse_int('one hundred one'))
print('200:', parse_int('two hundred'))
print('1:',parse_int('one'))
print('1 000 000:', parse_int('three million'))
print('246:', parse_int('two hundred forty-six'))
# print(parse_int('one million'))

