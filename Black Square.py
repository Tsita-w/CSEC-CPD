def calculate_calories(a1, a2, a3, a4, s):

    calories_map = {'1': a1, '2': a2, '3': a3, '4': a4}

    total_calories = 0


    for char in s:
        total_calories += calories_map[char]

    return total_calories


a1, a2, a3, a4 = map(int, input().split())
s = input()

print(calculate_calories(a1, a2, a3, a4, s))
