mot = input("Entrez un mot : ")
voyelles = "aeiouyAEIOUY"
compteur = 0
compteurs = 0
for lettre in mot:
    if lettre in voyelles:
        compteur += 1
    else :
        compteurs += 1
print("Nombre de voyelles :", compteur)
print("Nombre de consonnes :", compteurs)
