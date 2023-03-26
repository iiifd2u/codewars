def hamming(n):
    hemm = [2, 3, 5]
    arr =[1, 1, 1]
    s = [1]
    while len(s)<n:
        a, b, c =arr[0]*hemm[0], arr[1]*hemm[1], arr[2]*hemm[2]
        m = min(a, b, c)
        if m>s[-1]:
            s.append(m)
        x = [a, b, c].index(m)
        arr[x]=max(s[s.index(arr[x])+1], arr[x]+1)
    return s[-1]

print(hamming(5000))

