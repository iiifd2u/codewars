def spiralize(n):
    matrix = [[1 for _ in range(n)] for i in range(n)]
    r, c, k = 1, 0, 0
    rw, dw, lw, fw =n-1, n-1, 0, 0
    while k<=n//2:
        while c<rw:
            matrix[r][c]=0
            c+=1
        c-=1
        rw-=2
        while r<dw:
            matrix[r][c] = 0
            r += 1
        r-=1
        dw-=2
        fw += 2
        while c>lw:
            matrix[r][c] = 0
            c -= 1
        c+=1
        lw+=2
        while r>fw:
            matrix[r][c] = 0
            r -= 1
        r+=1
        k+=1
    return matrix




for row in spiralize(8):
    print(*row)