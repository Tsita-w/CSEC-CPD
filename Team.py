n = int(input("Enter the number of problems: "))
problems_solved = 0

for i in range(n):

    friends = list(map(int, input(f"Enter the views for problem {i+1} (Petya Vasya Tonya): ").split()))

    if sum(friends) >= 2:
        problems_solved += 1
print( problems_solved)
