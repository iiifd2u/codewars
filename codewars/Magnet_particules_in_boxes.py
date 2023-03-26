def v(k, n):
    return 1/(k*(n+1)**(2*k))

def double(maxk, maxn):
    result = 0
    for k in range(1, maxk+1):
        result += sum([v(k, n) for n in range(1, maxn+1)])
    return result



