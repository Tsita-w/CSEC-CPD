
matrix = []
one_position = (0, 0)

for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

    if 1 in row:
        one_position = (i, row.index(1))
center_position = (2, 2)
moves = abs(one_position[0] - center_position[0]) + abs(one_position[1] - center_position[1])
print(moves)
