def determinant(matrix):
    if len(matrix)==1:
        return matrix[0][0]
    else:
        det =0
        for idx, el in enumerate(matrix[0]):
            m=[]
            for i in range(1, len(matrix)):
                m.append([x for j, x in enumerate(matrix[i]) if j!=idx])
            det+=(-1)**idx*el*determinant(m)
        return det

print(determinant([[5]]))
print(determinant([[4, 6], [3, 8]]))
print(determinant([[2, 4, 2], [3, 1, 1], [1, 2, 0]]))
print(determinant([[2, 4, 2, 1], [3, 1, 1, 1], [1, 2, 0, 1], [1, 2, 2, 2]]))



