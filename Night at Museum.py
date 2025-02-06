def min_rotations(s):
    total_rotations = 0
    current_char = 'a'

    for target_char in s:
        clockwise_distance = abs(ord(current_char) - ord(target_char))
        counterclockwise_distance = 26 - clockwise_distance

        total_rotations += min(clockwise_distance, counterclockwise_distance)
        current_char = target_char

    return total_rotations
s = input().strip()

print(min_rotations(s))

