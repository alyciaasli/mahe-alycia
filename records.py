def record():
    nbJours = int(input())##demander le nombre de jour
    record = 0##initialiser le record a 0

    for _ in range(nbJours):##une boucle pour demander le nombre de jour
        distance = int(input())##demander la distance
        if distance > record:##comparer la distance avec le record
            record = distance##mettre a jour le record si la distance est superieur

    print(record)##afficher le record

record()
