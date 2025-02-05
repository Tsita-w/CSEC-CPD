def stones_to_remove(n, s):

    remove_count = 0
    for i in range(1, n):

        if s[i] == s[i - 1]:
            remove_count += 1

    return remove_count


n = int(input())
s = input()

print(stones_to_remove(n, s))
