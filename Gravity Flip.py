
n = int(input("Enter the number of columns: "))

cubes = list(map(int, input("Enter the number of cubes in each column: ").split()))

cubes.sort()

print(" ".join(map(str, cubes)))
