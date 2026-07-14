rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements:")
for i in range(rows):
    row = []
    for j in range(columns):
        value = int(input())
        row.append(value)
    matrix.append(row)

transpose = []

for i in range(columns):
    new_row = []
    for j in range(rows):
        new_row.append(matrix[j][i])
    transpose.append(new_row)

print("Transpose of the matrix:")

for row in transpose:
    print(row)