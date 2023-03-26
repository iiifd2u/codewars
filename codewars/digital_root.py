def digital_root(n):
    while len(list(str(n)))>1:
        n=sum(list(map(int, list(str(n)))))
    return n
    
def solution(s):
    if len(s)%2: s+='_'
    s=list(s)
    return [x+y for x, y in zip(s[::2], s[1::2])]