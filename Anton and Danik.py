
n = int(input("Enter the number of games: "))
s = input("Enter the outcomes of the games: ")

anton_wins = 0
danik_wins = 0

for game in s:
    if game == 'A':
        anton_wins += 1
    elif game == 'D':
        danik_wins += 1

if anton_wins > danik_wins:
    print("Anton")
elif danik_wins > anton_wins:
    print("Danik")
else:
    print("Friendship")
