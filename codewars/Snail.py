def snail(matrix):
    
    # for row in matrix:
    #     print(*[str(el).ljust(3) for el in row])
    r, c, k = 0, 0, 0
    rw, dw, lw, fw =n-1, n-1, 0, 0
    one_size=[]
    while k<=n//2:
        while c<rw:
            one_size.append(matrix[r][c])
            matrix[r][c]=0
            c+=1
        rw-=1
        while r<dw:
            one_size.append(matrix[r][c])
            matrix[r][c] = 0
            r += 1
        dw-=1
        fw += 1
        while c>lw:
            one_size.append(matrix[r][c])
            matrix[r][c] = 0
            c -= 1
        lw+=1
        while r>fw:
            one_size.append(matrix[r][c])
            matrix[r][c] = 0
            r -= 1
        k+=1
    # for row in matrix:
    #     print(*[str(el).ljust(3) for el in row])
    one_size.append(max([max(matrix[i]) for i in range(n)]))
    return one_size
