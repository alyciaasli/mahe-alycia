age = int(input("l'age de l'aubergiste : "))
poids = int(input("le poids du bagage : "))
prix = 0

if age  ==  60:
    prix = 0
elif age < 10:
    prix = 5
    print("Desole vous etes trop jeune pour rester seul")
elif 10 < age < 59 :
    prix = 30
    if poids >= 20:
        prix += 10
else :
    print("erreur de saisie")
print("le prix de la nuit est de ", prix, "euros")
