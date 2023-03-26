import string
def hamster_me(code:str, message:str):
    alpha = list(string.ascii_lowercase)
    code, message = code.lower(), message.lower()
    cd = {el[0]:[el[0]+'1'] for idx, el in enumerate(list(code))}
    av = {el[0]:[el[0]] for idx, el in enumerate(list(code))}
    for k, v in cd.items():
        i=2
        for a in alpha[alpha.index(k)+1:]+alpha[:alpha.index(k)+1]:
            #print('a({}) ={}'.format(v[0], a))
            if a not in cd.keys():
                cd[k].append(k+str(i))
                av[k].append(a)
                i+=1
            else:
                break
    text = ''
    # print('cd = ', cd)
    # print('av = ', av)
    for letter in list(message):
        for k, v in av.items():
            if letter in v:
                text+=cd[k][v.index(letter)]


    return text


print(hamster_me('hamster', 'helpme'))
print(hamster_me('hmster', 'hamster'))
print(hamster_me('hamster', 'hamster'))
print(hamster_me('f', string.ascii_lowercase))