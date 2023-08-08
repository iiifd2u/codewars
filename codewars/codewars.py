import math
import re

import numpy as np
# a = input()
# def no_space(x):
#     arr = x.split(" ")
#     return arr
# print(no_space(a))

# def calc(a, b, operation):
#     if operation == "+":
#         return a+b
#     elif operation == "-":
#         return a-b
#     elif operation == "*":
#         return a*b
#     elif operation == "/":
#         return a/b
#     else:
#         return "Операция не поддерживается"
# print((calc(15, 4, "f")))

# def nc(arr):
#     for i in arr:
#         if i == 139:
#             return
#         elif i%2 !=0:
#             print(i)
# print(nc([1, 2, 4, 139, 5]))


# n = np.empty(10, dtype='int8')
# print(n)
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# def create_phone_number(n):
#     n = [str(el) for el in n]
#     return f'({"".join(n[:3])}) {"".join(n[3:6])}-{"".join(n[6:])}'
# print(create_phone_number(x))
# a =[]
# for i in range(7):
#     n = (np.random.randint(0, 100), np.random.randint(-2, 26))
#     a.append(n)
#
# def open_or_senior(data):
#     new_date=[]
#     for elem in data:
#         if elem[0]>=55 and elem[1]>7:
#             new_date.append('Senior')
#         else:
#             new_date.append('Open')
#     return new_date
#
# def openOrSenior(data):
#   return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]
#
# print(open_or_senior(a))
# print(openOrSenior(a))
# n = 9119
#
# def square_digits(num):
#     return ''.join([str(int(el)**2 )for el in str(num)])
#
# print(square_digits(n))
# string = "8 -8 4 5 9 -10"
# def high_and_low(numbers):
#    a = [int(el) for el in numbers.split(' ')]
#    a.sort(reverse=True)
#    return str(a[0]) +' ' +str(a[-1])
   # if len(a) == 1
   #    return str(a[0])
   # return ' '.join([str(el) for el in a[0::len(a)-1]])
#
# print(high_and_low(string))

#Stepik

# num = int(input())


# a = []
# def counter(n):
#     for i in range(1, n+1):
#         for j in range(1, i+1):
#             a.append(i)
#     return a
# print(counter(num))
# def lenght(x):
#     return int((1+x)*x/2)

# def count(x, i=2):
#     while x <= rec(i):
#         i+=1
#         print(i)
#     return i

# num = int(input())
# a=[]
# def counter(n):
#     for i in range(1, n+1):
#         for j in range(1, i+1):
#             a.append(str(i))
#     return ' '.join(a[:num:])
# def rev_length(y):
#     return math.ceil((-1+math.sqrt(1+8*y))/2)
#
# print(counter(num))

# def beegeek(a, b):
#     if a>b:
#         a, b= b, a
#     li = [i for i in range(a, b+1)]
#     return ' '.join(list(map(validator, li)))
# def validator(el):
#     if el%3 == 0 and el%7 ==0:
#         el = 'BeeGeek'
#     elif el%3==0:
#         el = 'Bee'
#     elif el % 7==0:
#         el = 'Geek'
#     else:
#         el = str(el)
#     return el
#
# print(beegeek(1, 2))

# n = input()
# m = input()
#
# print(sorted(n), sorted(m))
# n_s=sorted(n)
# m_s=sorted(m)
# for n_el, m_el in n_s, m_s:
#     id n_el !=

# a=input()
# def f(el):
#     if el !='1':
#         return '0'
#     return '1'
# b =''.join(list(map(f, list('1'.join(('1'.join(a.split('|¯'))).split('|_'))))))
# print(b)

# nu = str(input()).split(' ')
# # nu.pop(-1)
# nu.sort(reverse=True)
# print(nu)
# i=0
#
# def poker(n):
#     d = {1: 1, 2: 1, 3: 1, 4: 1}
#     cur_mast = 1
#     for previous, current in zip(n, n[1:]):
#         if previous == current:
#             d[cur_mast]+=1
#             for i in range(1, 5):
#                 if d[i]==5:
#                     return 'Шулер'
#         else:
#             cur_mast+=1
#     if '4' in d.values():
#         return 'Каре'
#
# print(poker(nu))
# st =''
#
# def count(string):
#     li =list(set(string))
#     li.sort()
#     di={}
#     for el in li:
#         di.update({el:string.count(el)})
#     return di
#
# print(count(st))
# st = 'Nibvq fhppr ffngn yypbfgf'
# def rot13(message):
#     s=''
#     for el in message:
#         if 65<=ord(el)<=90:
#             s+=chr((ord(el)+13)%91 +((ord(el)+13)//91)*65)
#         elif 97<=ord(el)<=122:
#             s+=chr((ord(el)+13)%123 +((ord(el)+13)//123)*97)
#         else:
#             s+=el
#     return s
# print(rot13(st))


# a1 = ["arp", "live", "strong"]
#
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#
# def in_array(array1, array2):
#     st =' '.join(array2)
#     s =set()
#     for i in range(len(array1)):
#         if st.find(array1[i]) !=-1:
#             s.add(array1[i])
#     s=list(s)
#     s.sort()
#     return s
# print(in_array(a1, a2))
# import re
# def to_camel_case(s):
#     a=re.split(r'[-|_]', s)
#     return ''.join([a[0]]+list(map(lambda x:x[0].upper()+x[1:], a[1:])))
#
# s =input()
# print(to_camel_case(s))

# n=int(input())
# li = [1, 2, 3]
# a=[1, 3, 2]
# for i in range(3, n):
#     li = li+[el for el in range(len(a)+1, i+len(a)+1)]
#     a=a+sorted(li[len(a):len(a)+i+1], reverse=True)
# print(*a[:n])
# dict11 = {'one': 'eon', 'two': 'two', 'four': 'True'}
# dict22 = {'two': 'own', 'zero': '4', 'four': 'True'}
#
# def key_difference(dict1, dict2):
#     dict_res={}
#     for k, i in dict1.items():
#         if k in dict2.keys():
#             if i==dict2[k]:
#                 dict_res[k]='equal'
#             else:
#                 dict_res[k]='changed'
#         else:
#             dict_res[k] = 'deleted'
#     for k in dict2.keys():
#         if k not in dict_res:
#             dict_res[k] = 'added'
#     return dict_res
# print(key_difference(dict11, dict22))

# n=list(input())
# dict={}
# sum=0
# flag =False
# for el in n:
#     dict[el] =dict.get(el, 0)+1
# for k, v in dict.items():
#     if not flag and v%2!=0:
#         flag=True
#         sum+=1
#     sum+=(v//2)*2
#
#
# print(sum)

# coord =[int(el) for el in input().split()]
# colors = input().split()
# dict={'xer_sobachiy':[0]}
# mx=0
# for x, c in zip(coord, colors):
#     dict[c]=dict.get(c, [])+[x]
# for el in dict.values():
#     if max(el)-min(el)>mx:
#         mx = max(el)-min(el)
#
# print(mx)

# n=input()
# sum=1
# if len(set(n))==1:
#     sum=len(n)
# else:
#     for i in range(1, len(n)):
#         if n[:i]*int((len(n)/i)) ==n and len(n)%i==0:
#             sum =int(len(n)/i)
#
# print(sum)

# import re
# s = input()
# count = s.count('(')
# for _ in range(s.count('(')):
#     nums = re.findall(r'[0-9]+\([^0-9()]+\)', s)
#     for j in range(len(nums)):
#         ch = re.findall(r'[0-9]+', nums[j])
#         letters = re.findall(r'[^0-9()]+', nums[j])
#         s=s[:s.index(nums[j])]+int(ch[0])*letters[0]+ s[s.index(nums[j])+len(nums[j]):]
# print(s)

# print(ch)
# print(letters)
# print(s.index(nums[j]))
# print(s[:s.index(nums[j])])
# print(s[s.index(nums[j]) + len(nums[j]):])



# li =[el for el in colors if colors.count(el)>1]
#
# for x, c in zip(coord, colors):
#     if abs((dict.get(c, 0)-x))>dict.get(c, 0) and c in li:
#         dict[c] = abs(dict.get(c, 0)-x)
# print(max(dict.values()))

# n =[int(el) for el in input().split()]
# n.sort(key=lambda x:abs(x))
# vb =int(n[0]/abs(n[0]))
# sb=0
# rb=0
# catch=0
# while catch<1:
#     n[0]=n[0]+int(n[0]/abs(n[0]))
#     n[1] = n[1] + int(n[1] / abs(n[1]))
#     s = abs(n[0] - n[1])
#     sb=sb+vb*2
#     rb+=abs(vb*2)
#     if sb ==n[0] or sb ==n[1]:
#         catch=1
# print(s*2+rb)


# n=int(input())
# a=[1, 3, 2]
# m=math.ceil((math.sqrt(1+8*n)-1)/2)
# li=[el for el in range(1, n+m)]
# for i in range(3, n):
#     a=a+sorted(li[len(a):len(a)+i], reverse=True)
# print(*a[:n])

# l ='https://github.com/carbonfive/raygun'
# l1='www.xaker-com.com'
# import re
# def domain_name(url):
#     url = re.sub(r'www.|http://|https://', '', url)
#     r=re.match(r'\w+[-]\w+|\w+', url)
#     return r.group(0)
# print(domain_name(l))

# a = input()
# b=input()
# c=input()
# print(a)
# print(b)
# print(c)

# print(*[input() for _ in range(3)], sep='\n')
# l=359999
# def make_readable(seconds):
#     h=seconds//3600
#     m=(seconds-h*3600)//60
#     s=seconds%60
#     return '{}:{}:{}'.format(str(h).rjust(2, '0'), str(m).rjust(2, '0'), str(s).rjust(2, '0'))
# print(make_readable(l))

#ЗАДАЧА_1
# n=re.search(r'\d', input())
# print(n[::-1])
# n = int(input())
# n= ''.join([str(el) for el in range(1000)])
# for i in range(205):
#     print(f'{i}:{n[i]}')
# m=int(input())
# x=m
# for i in range(1, len(str(m))):
#     x+= 10**i
#     print(x)
# print(x/len(str(m)))


# ch_n = 55
# c=ch_n
# p=0
# while c>9:
#     c=c/10
#     p+=1
# print(p)
# ch_d =2*ch_n-10*p
# print(ch_d)

#ЗАДАЧА_2
# n=input()
# print(sum([int(el)+1 for el in n]))

#ЗАДАЧА_3
# n, m = [int(el) for el in input().split()]
# ar = [input() for _ in range(n)]
# for el in ar:
#     s = re.findall(r'[0-9a-zA-Z]+', el)
#     l=[f[::-1] for f in re.split(r'[0-9a-zA-Z]+', el)]
#     if len(s)>0:
#         for i in range(0, len(s)):
#             l.insert(i*2+1, s[i])
#     k=''.join(l[::-1])
#     print(k)

#ЗАДАЧА_4
# s = int(input())
# # d={0:'(', 1:')', 2:'[', 3:']'}
# # a=[[] for _ in range(2**s)]
# # for j in range(4):
# #     for el in a:
#
# from itertools import product
# for combos in product('()[]', repeat=s):
#     print(''.join(combos))

#ЗАДАЧА_5
# n=[el for el in input().split()]
#
# # for i in range(len(n)-1, 0, -1):
# #     print(f'i={i}')
# #     if n[i]<n[i-1]:
# #         n.remove(n[i])
# a=[]
# for i in range(1, len(n)-1):
#     print(i)
#     if n[i-1]<n[i] and n[i+1]<n[i]:
#         a.append(n[i-1])
#         a.append(n[i+1])

#
# print(a)

#ЗАДАЧА_6
# n=[int(el) for el in input().split()]
# ans ='False'
# for el in n:
#     if max(n)<=sum(n)//2:
#         n.remove(max(n))
#         print(n)





# for i in range(len(n)):
#     print(n[:i], n[i:])
#     if sum(n[:i]) ==sum(n[i:]):
#
#         ans='True'
#         break
# print(ans)

# import random
# n = 5
# matrix = [[random.randint(0, 50) for _ in range(n)] for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         print(str(matrix[i][j]).ljust(2), end=' ')
#     print()
# def snail(snail_map):
#     a=[]
#     c, r = 0, 0
#     n=len(snail_map)
#     if n ==1 and snail_map[n]==[]:
#         return a
#     for k in range(1, n+1):
#         while c<n-k:
#             a.append(snail_map[r][c])
#             c+=1
#         while  r< n - k:
#             a.append(snail_map[r][c])
#             r += 1
#         while c>=k:
#             a.append(snail_map[r][c])
#             c -= 1
#         while r>=k:
#             a.append(snail_map[r][c])
#             r -= 1
#         c, r = k, k
#     a.append(snail_map[n//2][n//2])
#     return a
#
# print(snail(matrix))

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# key = 'password'
# from typing import List
#
# class VigenereCipher(object):
#     def __init__(self, key, alphabet):
#         self.key = key
#         self.alphabet =alphabet
#         self.matrix = self.generate_matrix(alphabet)
#         self.dict_letters ={el:idx for idx, el in enumerate(alphabet)}
#         # for row in self.matrix:
#         #     print(row)
#
#     def generate_matrix(self, alphabet)->List[List[str]]:
#         L = len(alphabet)
#         matrix = []
#         for row in range(L):
#             current = alphabet[row:] + alphabet[:row]
#             matrix.append([el for el in current])
#         return matrix
#     def __generate_key(self, text):
#         text = text
#         new_psw = []
#         for idx, el in enumerate(list(text)):
#             new_psw.append(self.key[idx % len(self.key)])
#         return ''.join(new_psw)
#
#     def encode(self, text)->str:
#         new_psw = self.__generate_key(text)
#         new_word = []
#         # text = text.replace(' ', '')
#         for t, l in zip(list(text), new_psw):
#             if t not in list(self.alphabet):
#                 new_word.append(t)
#             else:
#                 new_word.append(self.matrix[self.dict_letters[l]][self.dict_letters[t]])
#         return ''.join(new_word)
#
#     def decode(self, text)->str:
#         new_psw = self.__generate_key(text)
#         new_decode = []
#         # text = text.replace(' ', '')
#         for t, l in zip(list(text), new_psw):
#             if t not in list(self.alphabet):
#                 new_decode.append(t)
#             else:
#                 row = self.matrix[self.dict_letters[l]]
#                 new_decode.append(self.alphabet[row.index(t)])
#         return ''.join(new_decode)
#
#
#
# c= VigenereCipher(key, alphabet)
# print(c.encode('my secret code i want to secure'))
# print(len('my secret code i want to secure'))
# print(len('passwordpasswordpasswordpasswor'))
# print(c.encode('codewars codewars'))
# print(c.decode('laxxhsj'))
# print(c.encode("CODEWARS"))
# print(c.decode("xt'kwgylutualvvu!"))



