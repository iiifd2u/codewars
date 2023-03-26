import re
import operator as o
def differentiate(equation, point):
    di ={'+':o.add, '-':o.sub}
    if equation[0]=='-':
        equation='0'+equation
    li = re.split(r'([\+\-\*\\])', equation)
    nums = li[::2]
    for idx, el in enumerate(nums):
        if el[0]=='x':
            nums[idx]='1x'+el[1:]
    #print(nums)
    signs = li[1::2]
    result =0
    list_nums = [dif(el, point) for el in nums]
    for i in range(len(list_nums)-1):
        result=di[signs[i]](list_nums[i], list_nums[i+1])
        list_nums[i]=0
        list_nums[i+1]=result
    return result



def dif(z, p):
    line = re.split(r'(x)\^?', z)
    if len(line)==1:
        a = 0
    elif line[-1]!='' and line[-1]!='x':
        a = int(line[0])*int(line[-1])*p**(int(line[-1])-1)
    else:
        a = int(line[0])
    return a

print(differentiare('-x^3-12x^2-3x+3', 3))
print(differentiare('-2x^2+x', 3))