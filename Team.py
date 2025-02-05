n = int(input())

solve_count = 0
for _ in range(n):
    
    p, v, t = map(int, input().split())
    

    if p + v + t >= 2:
        solve_count += 1
        
print(solve_count)

