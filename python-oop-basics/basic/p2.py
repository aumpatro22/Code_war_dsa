# Dynamic 2D matrix input from the user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
for r in range(rows):
    row = []
    for c in range(cols):
        value = int(input(f"Enter value for element [{r}][{c}]: "))
        row.append(value)
    matrix.append(row)

print("\nMatrix:")
for row in matrix:
    print(row)