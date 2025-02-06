def uniform_game(n, uniforms):
    total_matches = 0
    for i in range(n):
        for j in range(n):
            if i != j and uniforms[i][0] == uniforms[j][1]:
                total_matches += 1
    return total_matches

n = int(input())
uniforms = [tuple(map(int, input().split())) for _ in range(n)]

print(uniform_game(n, uniforms))
