def type():
    print("bonjour")
    a = input()
    print("oui ")

def marque():
    print("qu'elle est la marque de vos chaussures")
    marque_chaussure = input()

    if marque_chaussure == "nike":
        print("accepter")
    elif marque_chaussure == "jiselle":
            print("chaussure refuser")
    elif marque_chaussure == "adidas":
            print("chaussure refuser")
    else:
            print("refuser")
            type()

marque()