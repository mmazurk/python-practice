# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.


# 5, 5
# [0, 0, 0, 0, 0]
# [0, 1, 2, 3, 4]
# [0, 2, 4, 5, 8]
# [0, 3, 6, 9, 12]
# [0, 4, 8, 12, 16]

def rows_columns(rows, columns):
    final_matrix = []
    for i in range(0, columns):
        final_matrix.append([num * i for num in range(0,rows)])
  
    
    return final_matrix

rows_columns(5,5)