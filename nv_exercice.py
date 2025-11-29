n = int(input())
pairs = 0
impairs = 0
for _ in range(n):
    valeur = int(input())
    if valeur % 2 == 0:
        pairs += 1
    else:
        impairs += 1
print("Pairs :", pairs)
print("Impairs :", impairs)

