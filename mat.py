def matrix_multiply(matrix1, matrix2):
    result = []

    # Check if matrices can be multiplied
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")

    # Perform matrix multiplication
    for i in range(len(matrix1)):
        row_result = []
        for j in range(len(matrix2[0])):
            element_sum = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))
            row_result.append(element_sum)
        result.append(row_result)

    return result

# Get input from the user for the matrices
rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))

matrix1 = []
print("Enter the elements of the first matrix:")
for _ in range(rows1):
    row = [int(x) for x in input().split()]
    matrix1.append(row)

rows2 = int(input("Enter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))

matrix2 = []
print("Enter the elements of the second matrix:")
for _ in range(rows2):
    row = [int(x) for x in input().split()]
    matrix2.append(row)

# Perform matrix multiplication and display the result
result_matrix = matrix_multiply(matrix1, matrix2)
print("Result of matrix multiplication:")
for row in result_matrix:
    print(row)
