a = int(input("Enter Limak's weight: "))
b = int(input("Enter Bob's weight: "))

years = 0

while a <= b:
    a *= 3
    b *= 2
    years += 1

print( years)
