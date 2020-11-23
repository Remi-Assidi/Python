# -*- coding: utf-8 -*-
#!/usr/bin/python3

listeDesProduits = {1:{"Nom":"Banane","Prix":4.0,"Quantite":0}, 2:{"Nom":"Pomme","Prix":2.0,"Quantite":0}, 3:{"Nom":"Orange","Prix":1.5,"Quantite":0}, 4:{"Nom":"Poire","Prix":3.0,"Quantite":0}}

def display(listeDesProduits):
    prixTotal = 0.0
    print("+----------------------------------+---------+------------------------+----------------+")
    print("+------------NOM-------------------+--Prix---+--------Quantité--------+-----Total-HT---+")
    for produit in listeDesProduits:
        if listeDesProduits[produit]["Quantite"] != 0:
            totalht = listeDesProduits[produit]["Prix"]*listeDesProduits[produit]["Quantite"]
            print("|           {Nom}                 |   {Prix}   |          {Quantite}          |     {TotalHT}     |".format(Nom=listeDesProduits[produit]["Nom"], Prix=listeDesProduits[produit]["Prix"], Quantite=listeDesProduits[produit]["Quantite"], TotalHT=totalht))
            prixTotal += totalht
    print("+----------------------------------+---------+------------------------+----------------+")
    if prixTotal > 200:
        print("Sous total HT: {:.2f}".format(prixTotal))
        print("Remise 5%: {:.2f}".format(prixTotal-(prixTotal*0.95)))
        prixTotal = prixTotal*0.95
    print("Total HT: {:.2f}".format(prixTotal))
    print("Le prix total TTC est de {:.2f}".format(prixTotal*1.20))

def demanderQuantite():
    while True:
        quantite = float(input("Veuillez saisir la quantité: "))
        if quantite <= 0:
            print("Erreur votre quantite doit être supérieur à 0.")
        else:
            listeDesProduits[identifiant]["Quantite"] = quantite
            break

while True:
    identifiant = int(input("Veuillez saisir l'identifiant de votre produit: "))
    try:
        if identifiant in listeDesProduits.keys():
            demanderQuantite()
        else: 
            raise Exception("L'identifiant n'existe pas.")
    except Exception as e:
        print(e)
        print("Erreur, l'identifiant n'existe pas, veuillez reessayer.")
    saisirAutreProduit = input("Voulez vous saisir un autre produit ? (y/n) ")
    if saisirAutreProduit != "y":
        break
display(listeDesProduits)