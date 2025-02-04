
n = int(input("Enter the number of friends: "))
h = int(input("Enter the height of the fence: "))

heights = []
for i in range(n):
    height = int(input(f"Enter the height of friend {i+1}: "))
    heights.append(height)

total_width = 0

for height in heights:
    if height <= h:
        total_width += 1
    else:
        total_width += 2
        
print( total_width)
