rows_a = int(input("Enter number of rows in Matrix A: "))
cols_a = int(input("Enter number of columns in Matrix A: "))

matrix_a = []

print("Enter elements of Matrix A:")
for i in range(rows_a):
    row = []
    for j in range(cols_a):
        value = int(input())
        row.append(value)
    matrix_a.append(row)

rows_b = int(input("Enter number of rows in Matrix B: "))
cols_b = int(input("Enter number of columns in Matrix B: "))

matrix_b = []

print("Enter elements of Matrix B:")
for i in range(rows_b):
    row = []
    for j in range(cols_b):
        value = int(input())
        row.append(value)
    matrix_b.append(row)

if cols_a != rows_b:
    print("Error: Matrix multiplication is not possible.")
else:
    result = []

    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            row.append(total)
        result.append(row)

    print("Result Matrix:")
    for row in result:
        print(row)