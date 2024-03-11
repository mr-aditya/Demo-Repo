def transpose_matrix(matrix):
    # Use the zip function to transpose the matrix
    transposed_matrix = [list(row) for row in zip(*matrix)]
    return transposed_matrix

# Get input from the user for the matrix
rows = int(input("Enter the number of rows for the matrix: "))
cols = int(input("Enter the number of columns for the matrix: "))

matrix = []
print("Enter the elements of the matrix:")
for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

# Transpose the matrix and display the result
transposed_result = transpose_matrix(matrix)
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed_result:
    print(row)
