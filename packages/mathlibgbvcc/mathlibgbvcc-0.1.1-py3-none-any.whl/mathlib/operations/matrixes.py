def multiplication(matrix1, matrix2):
  if len(matrix1[0]) != len(matrix2):
    return None
  
  result = []
  
  for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix2[0])):
      row.append(sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1[0]))))
    result.append(row)
  return result
