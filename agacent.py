print("quelle et votre article a donner")
reponse = input()
prix = float(input("quelle est le prix de l'article : "))
if prix == 0:
    print("vous ne pouvez pas donner un article gratuit")
    
elif prix == 1:
    print("vous devez donner un article gratuit")
    print("fin")